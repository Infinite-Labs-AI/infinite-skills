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

2. Link a skill into Codex skills:

   ```bash
   mkdir -p ~/.codex/skills
   ln -s ~/.codex/infinite-skills/skills/goal ~/.codex/skills/goal
   ```

   Or install every skill:

   ```bash
   mkdir -p ~/.codex/skills
   for skill in ~/.codex/infinite-skills/skills/*; do
     ln -sfn "$skill" ~/.codex/skills/"$(basename "$skill")"
   done
   ```

3. Restart Codex.

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

Optionally remove the clone:

```bash
rm -rf ~/.codex/infinite-skills
```
