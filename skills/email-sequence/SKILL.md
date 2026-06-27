---
name: email-sequence
description: "Use when creating, auditing, or improving welcome, onboarding, nurture, activation, trial, abandoned cart, post-purchase, renewal, winback, or lifecycle email flows."
---

# Email Sequence

Plan lifecycle emails around what the customer has done, what they need next, and when they should stop receiving the flow.

## Map The State

Identify:

- Entry trigger.
- Recipient state and awareness.
- Product or offer relationship.
- Desired next action.
- What the user needs to believe or do first.
- Available personalization.
- Exit conditions.
- Compliance and deliverability constraints.

Do not write a sequence until the flow logic is clear.

## Plan The Flow

For each message, define:

- State: why they receive it now.
- Blocker: what prevents progress.
- Job: what it helps them understand or do.
- Proof or payload.
- CTA.
- Next observable behavior.
- Suppression or exit rule.
- Success signal.

Common arcs:

- **Welcome:** orient, prove fit, guide first action.
- **Trial activation:** remove setup friction, show quick win, invite human help.
- **Nurture:** teach problem, show alternatives, present offer.
- **Post-purchase:** confirm, help use, reduce regret, expand.
- **Winback:** acknowledge silence, offer relevant reason to return, suppress if uninterested.

## Write Messages

Keep copy specific to the state. Avoid generic appreciation, fake urgency, and repeating the same CTA in five costumes.

Every message needs one primary action. Secondary links are allowed only when they support the same job.

## Output

```text
Lifecycle flow:
Trigger:
Audience state:
Goal:
Exit conditions:

State transition map:
| Msg | Timing | Current state | Blocker | Message job | Next behavior | Exit/suppression |

Email draft:
Message [N]
Subject:
Preview:
Body:
CTA:

Setup notes:
- Segments:
- Personalization:
- Tests:
- Compliance checks:
```
