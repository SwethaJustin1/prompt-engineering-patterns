# Prompt Engineering Patterns for AI Strategy & Governance

A structured library of production-tested prompt templates for AI strategy, governance, and communications work.

Built and maintained by Sogibogi — AI Strategy & Responsible AI practitioner based in Pune, India.

---

## What this is

Most prompt libraries are built by engineers for engineers. This one is built for **AI leaders** — people making decisions about how AI is deployed, governed, and communicated inside organisations.

Every prompt in this library was designed to solve a specific business problem, tested against real inputs, and documented with its failure modes. The goal is not to showcase technical capability. The goal is to show what happens when someone who understands both AI systems and organisational strategy sits down to build tools for serious work.

---

## Who this is useful for

- AI Strategy leads evaluating enterprise AI deployments
- Responsible AI practitioners building governance workflows
- Communications leads translating AI for non-technical stakeholders
- Product managers designing AI-assisted decision processes

---

## Prompt Categories

| # | Category | Business problem it solves | Most relevant for |
|---|---|---|---|
| 01 | [Executive Summarisation](./prompts/01-executive-summarisation/prompt.md) | Convert long AI research or reports into board-ready briefings | All AI leadership roles |
| 02 | [Use Case Risk Classification](./prompts/02-use-case-risk-classification/prompt.md) | Classify proposed AI use cases by risk level and flag governance requirements | Responsible AI, Governance, Dataiku-type roles |
| 03 | [Stakeholder Translation](./prompts/03-stakeholder-translation/prompt.md) | Rewrite technical AI content for a specific non-technical audience | Communications, Policy, Partnerships roles |
| 04 | [Bias Audit](./prompts/04-bias-audit/prompt.md) | Systematically surface potential bias vectors in an AI output or system description | Responsible AI, Ethics, Anthropic/DeepMind roles |
| 05 | [Decision Support](./prompts/05-decision-support/prompt.md) | Structure an options analysis for an AI strategy or governance decision | Strategy, Product, Advisory roles |

---

## How to use these prompts

Each prompt file contains:
- **Business context** — the problem being solved and why a prompt approach is appropriate
- **The template** — with `[VARIABLES]` clearly marked for substitution
- **Example input** — a real scenario the template was tested on
- **Model notes** — tested on Claude Sonnet (Anthropic API); notes on output quality
- **Failure modes** — when this prompt produces poor results and why
- **When not to use this** — the situations where a different approach is needed

---

## Running these prompts

Use the included `run_prompt.py` script to test any prompt against the Anthropic API.

```bash
pip install anthropic
python run_prompt.py
```

Set your API key as an environment variable before running:
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

---

## Design principles

**1. Prompts are decisions, not instructions.**
A well-designed prompt encodes a judgment about what matters, what to ignore, and how to structure thinking. This is the same skill as writing a good strategy brief.

**2. Document failure modes.**
A prompt library without failure documentation is incomplete. Every template here includes the conditions under which it produces poor or misleading outputs.

**3. Business context before technical detail.**
Each prompt is introduced by its organisational use case, not its technical mechanism.

**4. Governance-aware by default.**
Several prompts explicitly include bias, risk, and transparency considerations built into the prompt design.

---

## Prompts added over time

| Date | Prompt | Notes |
|---|---|---|
| June 2026 | Executive Summarisation | Tested on 3 Anthropic research papers |
| June 2026 | Use Case Risk Classification | Modelled on EU AI Act risk tier logic |
| June 2026 | Stakeholder Translation | Tested across board, regulator, and journalist audiences |
| June 2026 | Bias Audit | Draws on NIST AI RMF bias categories |
| June 2026 | Decision Support | Tested on 2 real AI vendor evaluation decisions |

---


