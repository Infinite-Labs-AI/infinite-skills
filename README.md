# Infinite Skills

OpenAI recently launched /goal, a function that lets agents work towards an outcomt.

Their team recently published an article explaining how to get the most out of the new feature.
https://x.com/dkundel/status/2062650378089594955

I took the best practises shared article in the article and made it into a skill.

Infinite Skills is a small collection of agent skills for Codex, structured like
Superpowers: each skill lives in a flat `skills/<skill-name>/SKILL.md` directory.

## Skills

### goal

Preflight interview for Codex `/goal` mode. It clarifies a rough goal into a concrete,
verifiable contract before invoking goal mode with the full synthesized objective.

## Install For Codex

Clone this repository:

```bash
git clone https://github.com/Infinite-Labs-OS/infinite-skills.git ~/.codex/infinite-skills
```

Install the goal skill:

```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/infinite-skills/skills/goal ~/.codex/skills/goal
```

Restart Codex after installing so the new skill is discovered.

Detailed install notes are in [.codex/INSTALL.md](.codex/INSTALL.md).

## Layout

```text
skills/
  goal/
    SKILL.md
```

## License

MIT
