# Installing Infinite Skills For Codex

Enable Infinite Skills in Codex via local skill discovery.

## Prerequisites

- Git
- OpenAI Codex

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Infinite-Labs-AI/infinite-skills.git ~/.codex/infinite-skills
   ```

2. Link one skill into Codex skills:

   ```bash
   mkdir -p ~/.codex/skills
   ln -s ~/.codex/infinite-skills/skills/goal ~/.codex/skills/goal
   ```

   Or link every skill:

   ```bash
   mkdir -p ~/.codex/skills
   for skill in ~/.codex/infinite-skills/skills/*; do
     ln -sfn "$skill" ~/.codex/skills/"$(basename "$skill")"
   done
   ```

3. Restart Codex.

## Validation

Run this before publishing changes to the marketing skill set:

```bash
cd ~/.codex/infinite-skills
npm run validate
```

The validator checks that the curated marketing skills are present, discoverable, free of scaffold
placeholders, and materially distinct from the organized source corpus.

If you are validating without the original organized corpus on your machine, run:

```bash
ALLOW_MISSING_SOURCE_CORPUS=1 npm run validate
```

## Updating

```bash
cd ~/.codex/infinite-skills
git pull
```

The symlink points to the cloned repo, so updates are picked up after restart.

## Uninstalling

```bash
rm ~/.codex/skills/goal
rm ~/.codex/skills/launch-loop-strategy
```

If you linked every skill, remove the corresponding symlinks from `~/.codex/skills`.

Optionally remove the clone:

```bash
rm -rf ~/.codex/infinite-skills
```
