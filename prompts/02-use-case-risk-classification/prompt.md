# Prompt 02 — AI Use Case Risk Classification

## Business context

Every AI initiative inside an organisation starts with a use case. Most organisations have no systematic way to evaluate whether a proposed use case is safe to deploy — they either proceed without assessment or rely on gut instinct from whoever is most senior in the room.

This prompt provides a structured risk classification for any proposed AI use case. It is modelled on the EU AI Act risk tier logic and the NIST AI Risk Management Framework, translated into a format that a non-regulatory business audience can act on.

Designed for:
- AI strategy leads building a use case governance process
- Responsible AI practitioners evaluating deployment proposals
- Product managers who need to flag risk early before engineering investment
- Consultants running AI readiness assessments for enterprise clients

**Why a prompt approach works here:** Risk classification involves applying a consistent framework to varied inputs — a high-reliability LLM task when the framework is embedded in the prompt itself. The model is not making the governance decision; it is structuring the analysis. A human must make the final call.

---

## The template
---

## Failure modes

**1. Vague use case descriptions produce vague output.**
The more specific the input — who makes decisions, what happens to rejected cases, what data is used — the more actionable the output.

**2. The model cannot assess existing governance processes it cannot see.**
If the organisation already has mitigations in place, describe them in the input. Otherwise the model will flag risks that are already managed.

**3. This is analysis, not a decision.**
The output is a structured assessment to support a human governance decision. It should not be used as the governance decision itself.

---

## When not to use this

- Do not use for final regulatory compliance assessment — that requires a qualified compliance or legal professional.
- Do not use for use cases that are clearly unacceptable (mass surveillance, social scoring) — these should be declined without requiring a structured assessment.
- Do not present the output directly as your governance sign-off. A risk classification requires sign-off from a person with accountability.
