# Contributing to Infinite Skills

Thanks for improving Infinite Skills. The repository contains 25 marketing skills plus the Goal
skill for Codex; keep each skill scoped, discoverable, and materially distinct.

## Before opening a pull request

1. Fork the repository and create a focused branch from `main`.
2. Keep a skill in `skills/<skill-name>/SKILL.md`, with its matching `agents/openai.yaml` discovery
   metadata where required by the validator.
3. Do not add scaffold placeholders, source-corpus copy, unsupported frontmatter, or new generated
   artifacts unless the change explicitly needs them.
4. Describe the user-facing purpose, validation result, and any discovery/install impact in the pull
   request.

## Validate

When you have the original organized source corpus available, run:

```bash
npm run validate
```

When that corpus is unavailable, the required contribution gate is:

```bash
ALLOW_MISSING_SOURCE_CORPUS=1 npm run validate
```

The corpus-absent mode still validates the expected marketing-skill set, skill layout,
frontmatter, discovery metadata, headings, and content safeguards. It explicitly skips the
external-corpus 8-word shingle, normalized-line, and section-containment overlap checks. State
that limitation in your pull request; a passing corpus-absent run does not establish
corpus-distinctness.

## Install changes

If your change affects Codex discovery or installation, preserve the non-clobbering installer in
the README: it must leave existing files and unrelated symlinks untouched, report skipped targets,
and require the operator to move a conflicting target before rerunning it.

## Security

For ordinary repository reports, use the organization security policy when available. Do not put
credentials, private source material, or personal data in issues or pull requests.
