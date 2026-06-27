---
name: ab-testing
description: "Use when turning a marketing, growth, CRO, pricing, onboarding, email, ad, or acquisition idea into a useful experiment or test plan."
---

# A/B Testing

Turn a growth idea into a test that can actually change a decision.

## Frame The Decision

Start with the decision the experiment should inform:

- Ship, kill, iterate, scale, or investigate.
- Audience or surface being tested.
- Current baseline.
- Primary metric and guardrail metric.
- Minimum effect that would matter.
- Sample size or traffic reality.
- Time window and implementation cost.

If the traffic is too low for an A/B test, recommend a qualitative, sequential, or directional test instead.

## Write The Hypothesis

Use this shape:

```text
Because [observed problem], changing [specific thing] for [audience] should improve [primary metric] without hurting [guardrail], shown by [measurement].
```

Make the variant isolate one main idea. Do not mix headline, price, layout, offer, and audience changes unless the test is explicitly a bundled concept test.

## Choose The Test Type

Pick the method based on traffic, risk, and decision cost:

- **A/B test:** enough traffic and a reversible surface.
- **Before/after read:** operational change where randomization is impractical.
- **Concierge test:** validate demand or workflow manually before building.
- **Smoke test:** test interest before full fulfillment.
- **Fake-door test:** measure intent when the feature or offer is not ready, with ethical disclosure.
- **Qualitative read:** use interviews, session reviews, or sales calls when numbers will be too thin.

Add decision economics:

- Cost of shipping the wrong thing.
- Cost of waiting.
- Minimum useful evidence.

## Design The Test

Define:

- Control and variant.
- Inclusion and exclusion rules.
- Primary metric.
- Guardrails.
- Instrumentation requirements.
- Decision threshold.
- Stop conditions.
- Rollback plan.

## Interpret Carefully

- Do not call a winner before the decision threshold is met.
- Do not ignore novelty effects.
- Segment after the primary read, not until a desired story appears.
- Treat inconclusive results as useful when they eliminate bad ideas.

## Output

```text
Experiment brief:
Decision:
Hypothesis:
Audience:
Surface:

Evidence shape:
[A/B / before-after / concierge / smoke / fake-door / qualitative]

Decision economics:
- Cost of wrong ship:
- Cost of waiting:
- Minimum useful evidence:

Control or baseline:
Variant or intervention:

Metrics:
Primary:
Guardrails:
Instrumentation:

Readiness:
- Traffic:
- Baseline:
- Minimum useful lift:
- Runtime:

Decision rules:
- Ship if:
- Iterate if:
- Kill if:

Risks:
- [risk] -> [mitigation]
```
