#!/usr/bin/env python3
"""Simple keyword-based paper retrieval from JSONL database."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_DB_PATH = Path("data/papers.jsonl")


def normalize_text(text: str) -> str:
    return " ".join((text or "").strip().lower().split())


def load_papers(path: Path) -> list[dict[str, Any]]:
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


def tokenize(query: str) -> list[str]:
    return [tok for tok in re.split(r"[^a-zA-Z0-9\-\+]+", normalize_text(query)) if tok]


def textify(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value) if value is not None else ""


def score_paper(paper: dict[str, Any], query: str, tokens: list[str]) -> tuple[float, str]:
    title = normalize_text(textify(paper.get("title", "")))
    short_name = normalize_text(textify(paper.get("short_name", "")))
    category = normalize_text(textify(paper.get("category", "")))
    tags = normalize_text(textify(paper.get("tags", [])))
    task = normalize_text(textify(paper.get("task", [])))
    methods = normalize_text(textify(paper.get("method_family", [])))
    contribution = normalize_text(textify(paper.get("contribution", "")))

    query_norm = normalize_text(query)
    score = 0.0

    # Phrase bonus
    if query_norm and query_norm in title:
        score += 12
    elif query_norm and query_norm in contribution:
        score += 6

    fields = [
        (title, 4.0),
        (short_name, 2.5),
        (category, 2.0),
        (tags, 2.0),
        (task, 1.5),
        (methods, 1.5),
        (contribution, 1.0),
    ]

    for token in tokens:
        for field_text, weight in fields:
            if token and token in field_text:
                score += weight

    why = textify(paper.get("contribution", "")).strip()
    if not why:
        why = f"Related to {paper.get('category', 'computational pathology')}."
    why = why.replace("\n", " ")
    if len(why) > 140:
        why = why[:137] + "..."
    return score, why


def escape_md(text: str) -> str:
    return (text or "").replace("|", "\\|")


def main() -> None:
    parser = argparse.ArgumentParser(description="Query papers from JSONL knowledge base.")
    parser.add_argument("query", type=str, help="Query text")
    parser.add_argument("--topk", type=int, default=10, help="Top-K results (default: 10)")
    parser.add_argument(
        "--db",
        type=Path,
        default=DEFAULT_DB_PATH,
        help="Path to papers JSONL (default: data/papers.jsonl)",
    )
    args = parser.parse_args()

    papers = load_papers(args.db)
    if not papers:
        print("No matching papers found.")
        return

    tokens = tokenize(args.query)
    scored: list[tuple[float, int, dict[str, Any], str]] = []
    for paper in papers:
        score, why = score_paper(paper, args.query, tokens)
        year = int(paper.get("year", 0) or 0)
        if score > 0:
            scored.append((score, year, paper, why))

    if not scored:
        print("No matching papers found.")
        return

    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    top_results = scored[: max(args.topk, 1)]

    print("## Recommended Papers")
    print("")
    print("| Paper | Year | Venue | Category | Why it matters | Link |")
    print("|---|---:|---|---|---|---|")
    for _, year, paper, why in top_results:
        title = escape_md(textify(paper.get("title", "")))
        venue = escape_md(textify(paper.get("venue", "")))
        category = escape_md(textify(paper.get("category", "")))
        paper_url = textify(paper.get("paper_url", ""))
        why_text = escape_md(why)
        link = f"[paper]({paper_url})" if paper_url else ""
        print(
            f"| {title} | {year} | {venue} | {category} | {why_text} | {link} |"
        )


if __name__ == "__main__":
    main()
