# Infinite Skills

Infinite Skills is a collection of Codex skills for goal-setting and marketing operator work.
It contains 26 total skills: **25 marketing skills plus the Goal skill**. Each skill lives in a
flat `skills/<skill-name>/SKILL.md` directory.

Part of the [Infinite](https://infinite.fast/) ecosystem:

- [Infinite OS](https://github.com/Infinite-Labs-AI/infinite-os) is the local growth engine and CLI.
- [Infinite Agent Ecosystem](https://infinite.fast/agents/) shows the shipped public tools and their boundaries.
- [infinite.fast](https://infinite.fast/) is the main website.

The marketing set was designed from a review of a larger external marketing skill corpus, but it is
not a one-for-one remake. The repo keeps a smaller curated set with different names, workflows,
headings, deliverables, and validation checks.

## Skills

### Goal

- `goal` - Preflight interview for Codex `/goal` mode. It clarifies a rough goal into a concrete,
  verifiable contract before invoking goal mode with the full synthesized objective.

### Marketing

- `marketing-brief` - Product, audience, market, proof, channel, and next-action context.
- `customer-research` - Interviews, reviews, support tickets, surveys, and customer language.
- `positioning` - ICP, category, differentiation, and value proposition.
- `competitor-analysis` - Competitors, alternatives, win-loss themes, and battlecards.
- `offer-design` - Pricing, packages, guarantees, plans, trials, and upgrade paths.
- `marketing-plan` - Priorities, budgets, campaigns, calendar, reporting, and weekly execution.
- `launch-strategy` - Product launches, feature launches, launch checklists, waitlists, beta launches, and GTM rollouts.
- `launch-loop-strategy` - Practical 7-day feature launch loops: demo, post, share, reply, and repost.
- `distribution-plan` - Social, PR, community, newsletter, founder-led, and partner distribution.
- `content-strategy` - Blog, founder content, stories, examples, proof, and point of view.
- `x-article-writer` - Longform X/Twitter articles, founder essays, launch essays, and growth teardowns.
- `seo-strategy` - SEO pages, content clusters, site structure, and search acquisition.
- `ai-seo` - AI answers, LLM citations, entity clarity, and public proof.
- `copywriting` - Website, landing page, pricing, product, hero, value proposition, and CTA copy.
- `cro-audit` - Landing pages, signup, checkout, forms, onboarding, popups, and paywalls.
- `ecommerce-app-cro` - Ecommerce pages, carts, checkout, app listings, screenshots, and paywalls.
- `ab-testing` - Growth experiments, A/B tests, smoke tests, and decision-ready test plans.
- `email-sequence` - Welcome, onboarding, nurture, activation, winback, and lifecycle emails.
- `cold-outreach` - Cold email, LinkedIn outreach, prospecting, and founder-led direct outreach.
- `sales-enablement` - Decks, one-pagers, demos, follow-ups, objection handling, and champion assets.
- `partnerships` - Referrals, affiliates, co-marketing, creators, communities, and integrations.
- `paid-ads` - Paid acquisition across Google, Meta, LinkedIn, X, Reddit, TikTok, and sponsorships.
- `analytics-tracking` - GA4, GTM, UTMs, pixels, CRM attribution, funnel reporting, and dashboards.
- `retention` - Activation, churn, cancellation flows, winback, failed payments, renewal, and expansion.
- `creative-brief` - Ad, social, image, video, launch, UGC, and creator asset briefs.

## Install for Codex

Run this complete discovery installer. It clones (or fast-forwards) the checkout, links every
skill under `~/.codex/skills`, and never overwrites an existing file or a symlink that points
somewhere else. Review any `Skipped` line before moving that destination and rerunning it.

```bash
set -eu
repo_url="${INFINITE_SKILLS_REPO_URL:-https://github.com/Infinite-Labs-AI/infinite-skills.git}"
checkout="$HOME/.codex/infinite-skills"
skills_dir="$HOME/.codex/skills"
if [ -e "$checkout" ] || [ -L "$checkout" ]; then
  if [ ! -d "$checkout/.git" ]; then
    printf 'Cannot install: %s exists and is not an Infinite Skills git checkout.\n' "$checkout"
    exit 1
  fi
  git -C "$checkout" pull --ff-only
else
  mkdir -p "$HOME/.codex"
  git clone "$repo_url" "$checkout"
fi
mkdir -p "$skills_dir"
for skill in "$checkout"/skills/*; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  target="$skills_dir/$name"
  if [ -L "$target" ]; then
    current="$(readlink "$target")"
    if [ "$current" = "$skill" ]; then
      printf 'Already installed: %s\n' "$name"
    else
      printf 'Skipped %s: symlink points to %s; left untouched. Remove it and rerun to install this skill.\n' "$name" "$current"
    fi
  elif [ -e "$target" ]; then
    printf 'Skipped %s: destination exists; left untouched. Move it and rerun to install this skill.\n' "$name"
  else
    ln -s "$skill" "$target"
    printf 'Installed: %s\n' "$name"
  fi
done
```

Restart Codex after installation so it discovers the new skills. To install just one skill, use
the same non-clobbering checks above with that skill directory as the source.

## Validation

Run the marketing skill validator when the organized source corpus used during curation is
available:

```bash
npm run validate
```

The validator checks the curated 25-skill marketing set for expected directories, required
frontmatter, missing scaffold placeholders, source-style frontmatter, denied source phrases,
source-style headings, and discoverability metadata. With the corpus available it also checks
external-corpus slug, normalized-line, 8-word whole-file shingle, and 6-word section-containment
overlap.

When the original organized source corpus is not available, use:

```bash
ALLOW_MISSING_SOURCE_CORPUS=1 npm run validate
```

This mode still runs the structural and content checks above. It explicitly skips external-corpus
slug, 8-word shingle, normalized-line, and section-containment overlap comparisons, so it cannot
establish corpus-distinctness on its own.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution and validation gate.

## Layout

```text
skills/
  goal/
    SKILL.md
  launch-loop-strategy/
    SKILL.md
    agents/openai.yaml
  marketing-brief/
    SKILL.md
    agents/openai.yaml
  ...
scripts/
  validate_marketing_skills.py
```

## License

MIT
