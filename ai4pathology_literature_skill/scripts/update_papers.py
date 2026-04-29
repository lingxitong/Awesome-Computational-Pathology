#!/usr/bin/env python3
"""Update pathology AI papers from arXiv into a JSONL knowledge base."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime


ARXIV_API_URL = "http://export.arxiv.org/api/query"
DEFAULT_OUTPUT = Path("data/papers.jsonl")
DATE_FMT = "%Y-%m-%d"

ARXIV_QUERIES = [
    '"digital pathology"',
    '"computational pathology"',
    '"whole slide image"',
    '"histopathology"',
    '"pathology foundation model"',
    '"pathology vision language"',
    '"pathology multimodal"',
    '"multiple instance learning" AND pathology',
    '"slide-level" AND pathology',
    '"gigapixel" AND pathology',
    '"pathology agent"',
    '"medical image foundation model" AND pathology',
]

RELEVANT_KEYWORDS = [
    "pathology",
    "histopathology",
    "whole slide",
    "wsi",
    "digital pathology",
    "computational pathology",
    "gigapixel",
    "h&e",
    "tissue",
    "pathology report",
]

EXCLUDE_KEYWORDS = [
    "head ct",
    "computed tomography",
    "radiology",
    "mri",
    "diffusion weighted imaging",
    "quantum machine learning",
    "historical controls",
]

CATEGORY_RULES = [
    ("Surveys and Reviews", ["survey", "review"]),
    ("Datasets and Benchmarks", ["benchmark", "dataset", "leaderboard"]),
    (
        "Multiple Instance Learning",
        ["multiple instance learning", " mil ", "weakly supervised", "bag "],
    ),
    (
        "Federated Learning in Computational Pathology",
        ["federated", "privacy-preserving", "privacy preserving"],
    ),
    (
        "Patch-Level Foundation Models",
        [
            "foundation model",
            "self-supervised",
            "contrastive",
            "masked image modeling",
            "masked image",
            "patch-level",
            "tile-level",
        ],
    ),
    (
        "Slide-Level Foundation Models and Slide Encoders",
        ["whole slide", "wsi", "gigapixel", "slide encoder", "slide-level"],
    ),
    (
        "Vision-Language Models and Pathology Agents",
        [
            "vision-language",
            "vision language",
            "multimodal",
            "vqa",
            "report generation",
            "pathology agent",
            "large multimodal model",
            "vlm",
        ],
    ),
    (
        "Dense Prediction in Computational Pathology",
        [
            "segmentation",
            "detection",
            "nuclei",
            "gland",
            "cell detection",
            "dense prediction",
        ],
    ),
    (
        "Computational Pathology with Multi-Omics",
        [
            "omics",
            "transcriptomics",
            "spatial transcriptomics",
            "genomics",
            "mutation",
            "survival",
        ],
    ),
    (
        "Clinical Tasks and Applications",
        ["diagnosis", "prognosis", "grading", "subtyping", "biomarker"],
    ),
]

README_SECTION_TO_CATEGORY = {
    "surveys, reviews, and perspectives": "Surveys and Reviews",
    "datasets and benchmarks": "Datasets and Benchmarks",
    "multiple instance learning": "Multiple Instance Learning",
    "federated learning in computational pathology": "Federated Learning in Computational Pathology",
    "patch-level foundation models": "Patch-Level Foundation Models",
    "slide-level foundation models and slide encoders": "Slide-Level Foundation Models and Slide Encoders",
    "vision-language models and pathology agents": "Vision-Language Models and Pathology Agents",
    "dense prediction in computational pathology": "Dense Prediction in Computational Pathology",
    "computational pathology with multi-omics": "Computational Pathology with Multi-Omics",
    "clinical tasks and applications": "Clinical Tasks and Applications",
    "future trends and hot topics": "Future Trends and Hot Topics",
}


def normalize_text(text: str) -> str:
    return " ".join((text or "").strip().lower().split())


def normalize_title(title: str) -> str:
    cleaned = normalize_text(title)
    kept = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in cleaned)
    return " ".join(kept.split())


def slugify(text: str, max_len: int = 60) -> str:
    normalized = normalize_title(text).replace(" ", "-")
    slug = normalized.strip("-")[:max_len]
    return slug or "paper"


def load_existing(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    papers: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            papers.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return papers


def save_papers(path: Path, papers: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for item in papers:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def infer_category(title: str, abstract: str) -> str:
    text = f" {normalize_text(title)} {normalize_text(abstract)} "
    for category, keywords in CATEGORY_RULES:
        if any(keyword in text for keyword in keywords):
            return category
    return "Future Trends and Hot Topics"


def infer_tags(title: str, abstract: str, category: str) -> list[str]:
    text = normalize_text(f"{title} {abstract}")
    tags: set[str] = set()
    tag_rules = {
        "mil": ["multiple instance learning", " mil ", "attention mil"],
        "foundation-model": ["foundation model", "self-supervised", "ssl"],
        "wsi": ["whole slide", "wsi", "gigapixel"],
        "vlm": ["vision-language", "vision language", "multimodal", "vlm", "vqa"],
        "segmentation": ["segmentation", "nuclei", "gland"],
        "federated-learning": ["federated", "privacy-preserving"],
        "survival": ["survival", "prognosis"],
        "diagnosis": ["diagnosis", "subtyping", "grading"],
    }
    padded = f" {text} "
    for tag, keys in tag_rules.items():
        if any(key in padded for key in keys):
            tags.add(tag)
    if category:
        tags.add(category.lower().replace(" ", "-"))
    return sorted(tags)


def is_relevant(title: str, abstract: str) -> bool:
    text = normalize_text(f"{title} {abstract}")
    padded = f" {text} "
    if not any(keyword in padded for keyword in RELEVANT_KEYWORDS):
        return False
    if any(keyword in padded for keyword in EXCLUDE_KEYWORDS):
        return False
    return True


def extract_arxiv_id(entry: Any) -> str:
    if isinstance(entry, dict):
        raw = str(entry.get("id", "") or "")
    else:
        raw = getattr(entry, "id", "") or ""
    if not raw:
        return ""
    if "/abs/" in raw:
        return raw.split("/abs/")[-1]
    return raw.rsplit("/", 1)[-1]


def extract_year_from_text(text: str) -> int:
    full = re.findall(r"(?:19|20)\d{2}", text or "")
    if not full:
        return 0
    return int(full[-1])


def extract_arxiv_id_from_url(url: str) -> str:
    if not url:
        return ""
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", url)
    return match.group(1).replace(".pdf", "") if match else ""


def parse_readme_papers(readme_path: Path, today: str) -> list[dict[str, Any]]:
    if not readme_path.exists():
        return []

    lines = readme_path.read_text(encoding="utf-8").splitlines()
    current_category = "Future Trends and Hot Topics"
    parsed: list[dict[str, Any]] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            heading = normalize_text(stripped[3:])
            current_category = README_SECTION_TO_CATEGORY.get(heading, current_category)
            continue
        if not stripped.startswith("- **"):
            continue

        title_match = re.match(r"- \*\*(.+?)\*\*", stripped)
        if not title_match:
            continue

        title = " ".join(title_match.group(1).split())
        all_links = re.findall(r"\]\((https?://[^)]+)\)", stripped)
        external_links = [url for url in all_links if "img.shields.io" not in url]
        if not external_links:
            continue

        paper_url = external_links[0]
        for candidate in external_links:
            if "arxiv.org" in candidate or "doi.org" in candidate:
                paper_url = candidate
                break

        contribution = ""
        if "—" in stripped:
            contribution = stripped.split("—", 1)[1]
            contribution = re.sub(r"\[[^\]]+\]\((https?://[^)]+)\)", "", contribution).strip().strip(".")
            contribution = re.sub(r"\]\((https?://[^)]+)\)", "", contribution).strip().strip(".")

        badge_years = re.findall(r"%20((?:19|20)\d{2})-", stripped)
        badge_year = int(badge_years[-1]) if badge_years else 0
        url_year = extract_year_from_text(paper_url)
        year = badge_year or url_year or datetime.now().year
        arxiv_id = extract_arxiv_id_from_url(paper_url)
        category = current_category if current_category else infer_category(title, contribution)

        paper = {
            "id": f"{slugify(title, max_len=36)}-{year}-{(slugify(arxiv_id, 16) if arxiv_id else hashlib.md5(title.encode('utf-8')).hexdigest()[:8])}",
            "title": title,
            "short_name": "",
            "year": year,
            "venue": "README",
            "category": category,
            "type": "paper",
            "task": [],
            "method_family": [],
            "disease_or_organ": [],
            "modality": [],
            "contribution": contribution,
            "paper_url": paper_url,
            "code_url": "",
            "dataset_url": "",
            "model_url": "",
            "tags": infer_tags(title, contribution, category),
            "source": "readme",
            "arxiv_id": arxiv_id,
            "updated_at": today,
        }
        parsed.append(paper)
    return parsed


def query_arxiv(search_query: str, max_results: int) -> list[Any]:
    encoded_query = urllib.parse.quote(search_query)
    url = (
        f"{ARXIV_API_URL}?search_query=all:{encoded_query}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    )
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = response.read()

    root = ET.fromstring(payload)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
    }
    entries: list[dict[str, str]] = []
    for entry in root.findall("atom:entry", ns):
        links = entry.findall("atom:link", ns)
        primary_link = ""
        for link in links:
            href = link.attrib.get("href", "")
            rel = link.attrib.get("rel", "")
            if rel == "alternate" and href:
                primary_link = href
                break
            if not primary_link and href:
                primary_link = href

        entries.append(
            {
                "id": entry.findtext("atom:id", default="", namespaces=ns),
                "title": entry.findtext("atom:title", default="", namespaces=ns),
                "summary": entry.findtext("atom:summary", default="", namespaces=ns),
                "published": entry.findtext("atom:published", default="", namespaces=ns),
                "updated": entry.findtext("atom:updated", default="", namespaces=ns),
                "link": primary_link,
            }
        )
    return entries


def get_entry_field(entry: Any, field: str) -> str:
    if isinstance(entry, dict):
        return str(entry.get(field, "") or "")
    return str(getattr(entry, field, "") or "")


def parse_entry_datetime(raw: str) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip()
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = parsedate_to_datetime(raw)
        except (TypeError, ValueError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def convert_arxiv_entry(entry: Any, today: str) -> dict[str, Any]:
    title = " ".join(get_entry_field(entry, "title").split())
    abstract = " ".join(get_entry_field(entry, "summary").split())
    arxiv_id = extract_arxiv_id(entry)
    published_raw = get_entry_field(entry, "published") or get_entry_field(entry, "updated")
    published_dt = parse_entry_datetime(published_raw)
    year = published_dt.year if published_dt else datetime.now().year
    paper_url = get_entry_field(entry, "link") or f"https://arxiv.org/abs/{arxiv_id}"
    category = infer_category(title, abstract)
    paper_id = (
        f"{slugify(title, max_len=36)}-{year}-{slugify(arxiv_id, max_len=16)}"
        if arxiv_id
        else f"{slugify(title, max_len=36)}-{year}-{hashlib.md5(title.encode('utf-8')).hexdigest()[:8]}"
    )

    return {
        "id": paper_id,
        "title": title,
        "short_name": "",
        "year": year,
        "venue": "arXiv",
        "category": category,
        "type": "paper",
        "task": [],
        "method_family": [],
        "disease_or_organ": [],
        "modality": [],
        "contribution": abstract[:300] if abstract else "",
        "paper_url": paper_url,
        "code_url": "",
        "dataset_url": "",
        "model_url": "",
        "tags": infer_tags(title, abstract, category),
        "source": "arxiv",
        "arxiv_id": arxiv_id,
        "updated_at": today,
    }


def should_keep_by_date(entry: Any, min_date: datetime) -> bool:
    published_raw = get_entry_field(entry, "published") or get_entry_field(entry, "updated")
    if not published_raw:
        return True
    published_dt = parse_entry_datetime(published_raw)
    if published_dt is None:
        return True
    return published_dt >= min_date


def main() -> None:
    parser = argparse.ArgumentParser(description="Update pathology AI papers from arXiv.")
    parser.add_argument("--days", type=int, default=14, help="Look back N days (default: 14).")
    parser.add_argument(
        "--max-results",
        type=int,
        default=20,
        help="Max results per query from arXiv (default: 20).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output JSONL path (default: data/papers.jsonl).",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=None,
        help="Optional README path to import existing curated papers.",
    )
    args = parser.parse_args()

    today = datetime.now().strftime(DATE_FMT)
    min_date = datetime.now(timezone.utc) - timedelta(days=max(args.days, 0))
    existing = load_existing(args.output)

    known_arxiv_ids: set[str] = set()
    known_titles: set[str] = set()
    papers_by_key: dict[str, dict[str, Any]] = {}

    for paper in existing:
        arxiv_id = normalize_text(str(paper.get("arxiv_id", "")))
        title_key = normalize_title(str(paper.get("title", "")))
        if arxiv_id:
            known_arxiv_ids.add(arxiv_id)
            papers_by_key[f"arxiv:{arxiv_id}"] = paper
        if title_key:
            known_titles.add(title_key)
            papers_by_key.setdefault(f"title:{title_key}", paper)

    new_papers: list[dict[str, Any]] = []
    seen_run_ids: set[str] = set()
    seen_run_titles: set[str] = set()

    readme_new_papers: list[dict[str, Any]] = []
    if args.readme is not None:
        for paper in parse_readme_papers(args.readme, today):
            arxiv_id = normalize_text(str(paper.get("arxiv_id", "")))
            title_key = normalize_title(str(paper.get("title", "")))
            if arxiv_id and arxiv_id in known_arxiv_ids:
                continue
            if title_key and title_key in known_titles:
                continue
            if arxiv_id and arxiv_id in seen_run_ids:
                continue
            if title_key and title_key in seen_run_titles:
                continue
            readme_new_papers.append(paper)
            if arxiv_id:
                seen_run_ids.add(arxiv_id)
            if title_key:
                seen_run_titles.add(title_key)

    for query in ARXIV_QUERIES:
        try:
            entries = query_arxiv(query, args.max_results)
        except Exception as exc:  # pylint: disable=broad-except
            print(f"[WARN] query failed: {query} ({exc})")
            time.sleep(3)
            continue

        for entry in entries:
            title = " ".join(get_entry_field(entry, "title").split())
            abstract = " ".join(get_entry_field(entry, "summary").split())
            arxiv_id = normalize_text(extract_arxiv_id(entry))
            title_key = normalize_title(title)

            if not should_keep_by_date(entry, min_date):
                continue
            if not is_relevant(title, abstract):
                continue
            if arxiv_id and (arxiv_id in known_arxiv_ids or arxiv_id in seen_run_ids):
                continue
            if title_key and (title_key in known_titles or title_key in seen_run_titles):
                continue

            paper = convert_arxiv_entry(entry, today)
            new_papers.append(paper)
            if arxiv_id:
                seen_run_ids.add(arxiv_id)
            if title_key:
                seen_run_titles.add(title_key)

        time.sleep(3)

    merged = existing + readme_new_papers + new_papers
    merged.sort(key=lambda x: (int(x.get("year", 0)), normalize_title(str(x.get("title", "")))), reverse=True)
    save_papers(args.output, merged)

    total_new = len(readme_new_papers) + len(new_papers)
    if total_new == 0:
        print("No new papers found.")
        return

    print(f"Added {total_new} new papers.")
    for paper in (readme_new_papers + new_papers):
        print(
            f"- {paper['title']} | {paper['year']} | "
            f"{paper['category']} | {paper['paper_url']}"
        )


if __name__ == "__main__":
    main()
