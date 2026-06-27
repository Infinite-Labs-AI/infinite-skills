---
name: analytics-tracking
description: "Use when auditing, planning, or debugging marketing measurement, conversion tracking, GA4, GTM, UTMs, pixels, CRM attribution, funnel reporting, or dashboard trust."
---

# Analytics Tracking

Check whether marketing tracking is reliable enough to make decisions about budget, funnel performance, and growth.

## Start With Decisions

Ask what decisions the data is supposed to support:

- Which channel gets more budget.
- Which campaigns convert.
- Which pages or steps leak users.
- Which leads become revenue.
- Which lifecycle messages work.
- Which experiments win.

Tracking is not trustworthy because tags fire; it is trustworthy when the decision chain is complete.

## Inspect The Chain

Trace:

- Source capture: UTMs, referrer, click IDs, campaign naming.
- Event capture: page views, leads, signups, purchases, activation, qualified lead, revenue.
- Identity: anonymous to known user, lead to account, account to deal.
- Destination: analytics, ad platforms, CRM, warehouse, dashboards.
- Definitions: what counts as a conversion, lead, MQL, opportunity, customer.
- Consent and privacy boundaries.
- Reconciliation: totals across systems and expected gaps.

## Flag Trust Breaks

- Events fire but are not tied to the business outcome.
- Multiple systems define the same metric differently.
- UTMs overwrite or disappear.
- Test traffic pollutes reports.
- Duplicate conversions feed paid bidding.
- PII leaks into analytics or ad tools.
- Dashboards hide uncertainty.
- Offline revenue never connects back to campaigns.

## Judge Data Confidence

For each decision, state:

- Trust level: high, usable with caveats, directional only, not usable.
- Known gaps.
- Acceptable uncertainty.
- Reconciliation owner.
- Next check that would raise trust.

## Output

```text
Tracking trust read:
[one paragraph]

Decision chain:
Question -> Required signal -> Source -> Destination -> Owner

Decision trust:
| Decision | Trust level | Known gaps | Acceptable uncertainty | Reconciliation owner |

Trust breaks:
| Break | Evidence | Decision affected | Fix | Priority |

Measurement plan:
| Event | Trigger | Parameters | Destination | Success criteria |

Naming rules:
- [UTM or event rule]

Reconciliation checks:
1. [check]
2. [check]

Privacy risks:
- [risk]
```
