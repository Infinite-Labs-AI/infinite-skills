# Infinite Skills

Infinite Skills is a collection of Codex skills for goal-setting and marketing operator work.
Each skill lives in a flat `skills/<skill-name>/SKILL.md` directory.

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
- `launch-strategy` - Product launches, feature releases, waitlists, beta launches, and GTM rollouts.
- `launch-loop-strategy` - Practical 7-day feature launch loops: demo, post, share, reply, and repost.
- `distribution-plan` - Social, PR, community, newsletter, founder-led, and partner distribution.
- `content-strategy` - Blog, founder content, stories, examples, proof, and point of view.
- `seo-strategy` - SEO pages, content clusters, site structure, and search acquisition.
- `ai-seo` - AI answers, LLM citations, entity clarity, and public proof.
- `copywriting` - Landing page, website, pricing, product, ad, and CTA copy.
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

## Install For Codex

Clone this repository:

```bash
git clone https://github.com/Infinite-Labs-AI/infinite-skills.git ~/.codex/infinite-skills
```

Install one skill:

```bash
mkdir -p ~/.codex/skills
ln -s ~/.codex/infinite-skills/skills/goal ~/.codex/skills/goal
```

Install every skill:

```bash
mkdir -p ~/.codex/skills
for skill in ~/.codex/infinite-skills/skills/*; do
  ln -sfn "$skill" ~/.codex/skills/"$(basename "$skill")"
done
```

Restart Codex after installing so the new skill is discovered.

Detailed install notes are in [.codex/INSTALL.md](.codex/INSTALL.md).

## Validation

Run the marketing skill validator:

```bash
npm run validate
```

The validator checks the curated 24-skill marketing set for required frontmatter, missing scaffold
placeholders, source-style frontmatter, denied source phrases, source-style headings, discoverability
metadata, exact source-line overlap, excessive 8-word whole-file overlap, and excessive 6-word
section-level overlap with the organized source corpus.

By default, validation expects the organized source corpus to exist at the local path used during
creation. Set `ALLOW_MISSING_SOURCE_CORPUS=1` only when validating this repo without that corpus
available.

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
