# Prompt 05 — Decision Support

## Business context

AI strategy decisions are rarely binary. They involve multiple options, competing priorities, uncertain information, and stakeholders with different risk tolerances. Most organisations either make these decisions informally or over-engineer them with committee processes that slow everything down.

This prompt produces a structured options analysis for any AI strategy or governance decision. It is designed for the moment before a meeting — when you need to arrive with a clear-headed view of the options, the trade-offs, and the questions that need to be answered before a decision is made.

Designed for:
- AI strategy leads preparing recommendations for senior leadership
- AI product leads evaluating build/buy/partner decisions
- Responsible AI practitioners structuring a governance recommendation
- Interview preparation — any question beginning "How would you approach deciding..."

**Why a prompt approach works here:** Structured options analysis requires systematically applying a consistent evaluation framework to multiple alternatives — a high-reliability LLM task when the decision context and evaluation criteria are clearly specified.

---

## The template
---

## Failure modes

**1. False options produce false analysis.**
If the options given are not genuinely different strategic choices, the analysis will produce superficially different descriptions of the same approach. Test options by asking: would a reasonable person genuinely choose differently between these?

**2. The model cannot know your organisation.**
Internal dynamics, relationship history, and organisational politics that are not described will not appear in the analysis. Add them explicitly if they are decision-relevant.

**3. Anchoring on the stated options.**
If the right answer is an option you have not considered, the model will not volunteer it unless you explicitly ask: "What option am I not considering that I should be?"

---

## When not to use this

- Do not use for decisions that have a clearly dominant option — if the choice is obvious, you need permission to act, not a structured analysis.
- Do not use as a substitute for stakeholder consultation. A decision that affects your team requires their input.
- Do not present the output directly to a decision-maker as your analysis. This is your thinking tool. Rewrite in your own voice before presenting.
