---
name: paid-ads
description: "Use when reviewing or planning paid acquisition across Google, Meta, LinkedIn, X, Reddit, TikTok, sponsorships, retargeting, or other paid channels."
---

# Paid Ads

Review paid acquisition to decide what to cut, fix, test, or scale.

## Required Context

Use available platform exports, screenshots, campaign structure, UTMs, landing pages, CRM data, or spend summaries. If data is missing, ask for:

- Channel and objective.
- Spend, conversions, revenue, CAC, CPA, ROAS, or pipeline.
- Attribution window and conversion definition.
- Audience and offer.
- Creative examples.
- Landing page.
- Budget and time period.

Do not infer performance from structure alone when spend and conversion data exist.

## Diagnose The System

Inspect:

- **Economics:** target CAC/CPA, payback, LTV, gross margin, sales cycle.
- **Signal:** conversion tracking quality and event meaning.
- **Structure:** campaign objective, segmentation, budget allocation, bidding logic.
- **Audience:** targeting, exclusions, intent, saturation.
- **Creative:** message variety, proof, format fit, fatigue.
- **Landing path:** match between ad promise and page.
- **Learning:** what tests have been run and what changed.

Give the data a confidence grade before recommending budget moves. Weak tracking should produce repair or learn recommendations, not scale recommendations.

## Classify Issues

- **Tracking issue:** data cannot support decisions.
- **Offer issue:** click interest does not convert.
- **Message issue:** creative attracts wrong or weak intent.
- **Audience issue:** targeting is too broad, too narrow, or stale.
- **Economics issue:** campaign works mechanically but cannot pay back.
- **Scale issue:** winner exists but budget, creative, or funnel cannot absorb more.

## Output

```text
Paid acquisition read:
[one paragraph]

Current numbers:
Spend:
Conversions:
CPA/CAC:
Revenue/ROAS:
Confidence in tracking:

Classification:
[stop / repair / learn / scale]

Diagnosis:
| Area | Finding | Evidence | Severity | Next move |

Budget moves:
- Increase:
- Hold:
- Cut:

Tests:
1. [test]
2. [test]
3. [test]

Data needed before scaling:
- [missing signal]
```
