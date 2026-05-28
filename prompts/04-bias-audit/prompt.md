# Prompt 04 — Bias Audit

## Business context

Most organisations deploying AI systems do not conduct structured bias assessments before go-live. When they do, the assessment is often reactive — triggered by a complaint or incident — rather than systematic. By then, harm has already occurred.

This prompt provides a structured pre-deployment bias audit framework that any AI practitioner or strategy lead can apply to an AI system description. It does not replace a technical bias audit conducted by a data scientist. It surfaces the questions that a technical audit should answer — and identifies the bias vectors most likely to be present before anyone looks at the data.

Designed for:
- Responsible AI leads and ethics practitioners at any organisation
- AI strategy leads conducting pre-deployment governance reviews
- Product managers building AI features who want to flag risk early
- Interview preparation for Anthropic, Wadhwani AI, and Google DeepMind roles

**Why a prompt approach works here:** Bias identification requires systematically applying a framework of known bias categories to a specific system description. The output is a checklist for human investigation — not a definitive audit.

---

## The template
---

## Failure modes

**1. The model cannot assess data it cannot see.**
This prompt identifies likely bias vectors from a system description. It cannot confirm whether those biases are actually present in the training data. The output is a hypothesis list, not a confirmed finding.

**2. Vague system descriptions produce vague output.**
Invest time in the system description — who makes decisions, what data is used, who is affected.

**3. The model may miss India-specific context.**
Caste, regional language, and urban-rural dynamics may require explicit prompting. Add "Pay particular attention to caste, language, and urban-rural equity dimensions relevant to the Indian context" when relevant.

---

## When not to use this

- Do not use as a substitute for a technical bias audit with access to actual training data and model outputs.
- Do not use to produce a bias certificate — this prompt identifies questions to investigate, not answers that confirm safety.
- Do not use without reading the output critically and adding domain context the model cannot know.
