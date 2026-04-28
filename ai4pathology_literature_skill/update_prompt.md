# Update Prompt for AI4DigitalPathology Literature Skill

Use this prompt when updating the repository with new papers.

```text
You are maintaining the Awesome-AI4DigitalPathology knowledge base.

Task:
Update the literature/resource list for the following scope:
- Category: {category}
- Time range: {time_range}
- Target venues/sources: {venues_or_sources}
- Required resource type: {paper|dataset|benchmark|code|model|survey|toolkit|all}

For each candidate, produce:
1. normalized JSON record using the canonical schema;
2. README Markdown entry using the repository badge style;
3. category placement and reason;
4. whether the paper should be added, skipped, or verified.

Rules:
- Do not invent metadata.
- Prefer official paper, code, dataset, and model URLs.
- Keep README descriptions short.
- Avoid duplicates.
- If uncertain, mark `metadata_to_verify`.
```
