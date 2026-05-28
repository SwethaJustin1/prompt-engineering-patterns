# Prompt 01 — Executive Summarisation

## Business context

AI research papers, policy documents, and technical reports are routinely 20–80 pages long. Board members, senior leaders, and government partners have 3–5 minutes of attention available. 
The gap between those two realities is where AI communications lives.

This prompt converts any long AI document into a structured executive briefing that a non-technical senior leader can act on. It is designed for:
- Briefing a board on an AI research development
- Summarising a policy document (e.g. EU AI Act update, India AI Mission report) for leadership
- Preparing a client-facing summary of an AI vendor's capability paper
- Distilling a competitor's AI announcement into a strategic assessment

**Why a prompt approach works here:** Summarisation with a fixed output structure is one of the highest-reliability LLM tasks.
The failure modes are manageable and documented below.

---

## The template
---

## Failure modes

**1. The model flattens nuance in technical documents.**
If the source document contains important caveats, the model may present a cleaner conclusion than the document actually supports. Mitigation: add "Flag any conflicting evidence or unresolved tensions in the source document" to the prompt.

**2. The model invents specificity.**
For documents with vague claims, the model may produce precise-sounding summaries that are more confident than the source warrants. Always cross-reference against the original before sending to a real audience.

**3. Audience framing matters enormously.**
The same document summarised for a "board member" versus a "government minister" produces substantively different outputs. Test multiple audience framings for important documents.

---

## When not to use this

- Do not use for documents where legal or regulatory precision is required — a qualified professional must review any AI summary before use in a formal context.
- Do not use for documents you have not read yourself. This prompt accelerates your first pass — it does not replace your judgment.
- Do not use for real-time documents where the model has no access to dynamic context.
