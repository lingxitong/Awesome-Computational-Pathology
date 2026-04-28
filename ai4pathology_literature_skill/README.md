# AI4DigitalPathology Literature Skill Package

This package contains a ready-to-use skill specification for maintaining and querying an AI4DigitalPathology literature knowledge base.

It is developed based on [Awesome-AI4DigitalPathology](https://github.com/lingxitong/Awesome-AI4DigitalPathology).

Files:

- `SKILL.md`: main skill instruction file.
- `papers.schema.json`: structured JSON schema for paper/resource indexing.
- `update_prompt.md`: prompt template for automatic or manual literature updates.
- `query_prompt.md`: prompt template for answering user questions from the knowledge base.

Suggested installation:

```bash
mkdir -p <your-skill-directory>/ai4digitalpathology_literature
cp -R ai4digitalpathology_literature <your-skill-directory>/
```

Replace `<your-skill-directory>` with the skill path used by your local agent runtime.

For full functionality, maintain a `papers.jsonl` index alongside the README so the agent can query structured metadata quickly.
