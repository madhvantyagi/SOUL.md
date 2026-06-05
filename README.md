<p align="center">
  <img src="assets/soulimage.png" alt="SOUL.md banner showing an agent persona over a world map" width="100%" />
</p>

<h1 align="center">SOUL.md</h1>

<p align="center">
  <strong>A library of agent souls: portable persona files for AI systems that should behave with identity, taste, and conviction.</strong>
</p>

<p align="center">
  <a href="https://soul.md/"><img alt="Read soul.md" src="https://img.shields.io/badge/read-soul.md-111111?style=for-the-badge" /></a>
  <a href="https://www.stanza.dev/concepts/openclaw-soul-persona"><img alt="OpenClaw SOUL persona" src="https://img.shields.io/badge/OpenClaw-SOUL%20persona-2b6cb0?style=for-the-badge" /></a>
  <a href="https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/personality.md"><img alt="Hermes personality layer" src="https://img.shields.io/badge/Hermes-personality%20layer-5b21b6?style=for-the-badge" /></a>
  <a href="https://opencode.ai/docs/rules/"><img alt="OpenCode instructions" src="https://img.shields.io/badge/OpenCode-instructions-0f766e?style=for-the-badge" /></a>
</p>

---

## What Is This Repo?

This repository is a collection of `SOUL.md` files.

Each file is a reusable personality layer for an AI agent. You can use these souls with systems like OpenClaw, Hermes, OpenCode, Claude, ChatGPT, Gemini, local models, or any agent that can read Markdown instructions.

The point is to give agents **distinct personalities**, not the same polite default voice.

A strong persona changes how an agent thinks, pushes back, and works. The same model can feel totally different depending on the soul you load. Some personalities are unexpectedly strong at certain jobs: better conversation, clearer math, tighter follow-through on orders, or healthy disagreement when you need a second opinion instead of automatic agreement.

These files set that identity so the agent stays in character whether it is coding, researching, teaching, planning, or talking with you under pressure.

---

## What Is A SOUL.md File?

A `SOUL.md` file defines who an agent is.

It is not a task prompt. It is not a project setup file. It is not a list of tools. It is the personality and behavioral center of an agent:

| It defines | What that means |
| --- | --- |
| Identity | What kind of agent this is, what shaped it, and what it cares about. |
| Tone | The emotional temperature the user feels while interacting with it. |
| Convictions | The beliefs that make the agent predictable instead of generic. |
| Uncertainty | How the agent behaves when the answer is incomplete, risky, or unclear. |
| Pushback | What the agent challenges instead of blindly accepting. |
| Hard stops | What the agent never does in style, behavior, or collaboration. |

A weak instruction says:

```text
You are a helpful assistant. Be clear and professional.
```

A stronger soul says:

```text
You are a pragmatic systems engineer who has shipped and broken enough production
services to permanently lose patience for clever code. You value operational
reality over architectural elegance.
```

That second version gives the model a point of view. It can now make decisions in character.

---

## Recommended Reading

Before writing or using a soul file, read these:

| Read | Why it matters |
| --- | --- |
| [soul.md](https://soul.md/) | The core idea behind a soul document for agent identity and continuity. |
| [OpenClaw SOUL.md & Agent Persona](https://www.stanza.dev/concepts/openclaw-soul-persona) | Shows `SOUL.md` as a primary persona file in an agent bootstrap system. |
| [Hermes Personality & SOUL.md](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/personality.md) | Explains how Hermes treats `SOUL.md` as the first identity layer. |
| [OpenCode rules](https://opencode.ai/docs/rules/) | Shows how Markdown instruction files and remote URLs can be loaded by an agent workflow. |
| [AGENTS.md](https://agents.md/) | Useful for separating project rules from agent personality. |

Keep this distinction clean: `SOUL.md` is the agent's character. `AGENTS.md` is how it should work inside a project.

---

## Use A Soul In 30 Seconds

1. Open a soul file in this repository.
2. Click **Raw** on GitHub.
3. Copy the raw file URL.
4. Tell your agent:

```text
Read this SOUL.md and adopt this personality for the rest of the session:
https://raw.githubusercontent.com/madhvantyagi/SOUL.md/main/souls/<personality>/SOUL.md

Keep all existing project, tool, and safety instructions intact.
```

Replace `<personality>` with the soul you want to use.

If your agent cannot fetch URLs, copy the file contents directly into the agent's system prompt, custom instructions, `SOUL.md`, `AGENTS.md`, or personality configuration.

---

## Where You Can Use It

| Agent or tool | How to use it |
| --- | --- |
| OpenClaw | Save the chosen file as `SOUL.md` in the agent workspace, or ask the agent to read the raw URL. |
| Hermes Agent | Copy the chosen file into `~/.hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`. |
| OpenCode | Add the raw URL or local path to `opencode.json` `instructions`, or reference it from `AGENTS.md`. |
| Claude / ChatGPT / Gemini | Paste the soul above the task or place it in the custom instruction area. |
| Local models | Put the soul in the system prompt or agent bootstrap prompt. |
| Coding agents | Link the soul from `AGENTS.md`, `CLAUDE.md`, rules files, or other instruction files. |

---

## What Makes A Soul Good?

Good souls are not louder. They are more legible.

| Quality | What to look for |
| --- | --- |
| Specific | The agent has a worldview, not a vague job title. |
| Predictive | A reader can guess how the agent would handle a new situation. |
| Stable | The personality survives long sessions, messy prompts, and pressure. |
| Useful | The soul improves the work instead of performing personality for its own sake. |
| Portable | The file works across multiple models and agent tools. |
| Testable | You can prove the behavior changed by running prompts before and after. |

If the soul only changes vocabulary, it is shallow. If it changes judgment, prioritization, disagreement style, and emotional pressure, it is working.

---

## How To Test Agent Personality After A Soul

A soul file is a claim. You still need proof on the agent you run (Hermes, OpenClaw, OpenCode, or your own stack).

**Tool:** [trait-8000](trait-8000/) runs the [TRAIT](https://huggingface.co/datasets/mirlab/TRAIT) benchmark (~8,000 scenario questions). It scores what the model **chooses**, not what it says about itself.

**Traits measured**

- **Openness**, **Conscientiousness**, **Extraversion**, **Agreeableness**, **Neuroticism**
- **Machiavellianism**, **Narcissism**, **Psychopathy**

**Steps**

1. Read [trait-8000/README.md](trait-8000/README.md) for setup and scoring.
2. Load your soul and wire `call_llm_api()` to the same agent path you use in practice.
3. Run TRAIT. Compare the chart and `trait_evaluation_results.txt` to the personality you wrote.

**What you are checking**

- Outgoing soul → higher **Extraversion**
- Disciplined soul → higher **Conscientiousness**
- Calm soul → lower **Neuroticism**
- (Same idea for the other traits)

**What you are not doing**

- Comparing against a run with no soul loaded
- You are checking **fit**: do scores sit near the trait profile this character should show?

If key traits miss by a lot, the soul may not be reaching the model, or the file needs another pass. Details: [trait-8000/README.md](trait-8000/README.md).

---

## Contribution Guide

Contribute a soul when it adds a personality someone would choose on purpose.

Do not add a generic assistant with nicer wording. Add an agent with a recognizable way of thinking, speaking, deciding, and pushing back.

### 1. Pick A Personality, Not A Job Title

Add one file:

```text
souls/<personality-slug>/SOUL.md
```

- **Good slug** — names a character: `jarvis`, `gojo`, `rene-descartes`
- **Weak slug** — names a job: `helpful-coder`, `friendly-assistant`

**Examples**

- `souls/jarvis/SOUL.md` — calm, technical, anticipatory
- `souls/gojo/SOUL.md` — playful mentor, serious when stakes rise

Browse `souls/` in this repository.

### 2. Make Every Section Earn Its Place

The soul should change **behavior**, not just word choice.

**Include** (see [Suggested SOUL.md Shape](#suggested-soulmd-shape))

- Identity (and optional purpose)
- Tone
- Convictions as tradeoffs (belief → behavior)
- Uncertainty
- Pushback
- Hard stops
- How you meet the user (by context)
- When the user is wrong (low / high stakes / harmful premise)
- Voice and examples (when register matters)
- Boundaries (persona-level only)

**Do not put in `SOUL.md`**

- Project commands, ports, file paths, setup steps, or test workflows
- Tool permissions, destructive-action rules, or external-send policies
- Secrets, credentials, private data, or temporary preferences
- Repo architecture, coding conventions, or implementation checklists

Those belong in `AGENTS.md`, `CLAUDE.md`, rules files, hooks, policies, or memory.

**Cut or rewrite** any section that does not change how the agent acts under pressure.

### 3. Test Before Contributing

A soul is not ready because it reads well. It is ready when behavior changes on real agents and models.

| Where to test | What to check |
| --- | --- |
| Your agent (Hermes, OpenClaw, coding agent, etc.) | Does the soul load on the path you use in production? |
| More than one model | Does the persona hold on a strong model and a smaller local one? |
| [trait-8000](trait-8000/) | Run TRAIT with the soul loaded. Do scores match the trait profile this personality is supposed to have? |

Try a few real tasks in chat, then run TRAIT on scenario questions. When you open a PR, note which agents and models you tested and which TRAIT traits lined up with (or missed) the soul you intended.

---

## Suggested SOUL.md Shape

This is a recommended shape, not a hard rule. A soul can be shorter, stranger, more poetic, or more technical, as long as it gives the agent a coherent identity.

`SOUL.md` defines stable persona-level behavior: identity, judgment, voice, tone, correction style, uncertainty handling, and persona boundaries. It does not override system or developer instructions, safety rules, tool permissions, `AGENTS.md`, `CLAUDE.md`, repo rules, project workflows, or valid user instructions.

Also add `souls/<personality-slug>/README.md` with a one-line pitch, traits, one short dialogue example, and the [raw load snippet](#use-a-soul-in-30-seconds).

**Length targets**

| Soul type | Target | Notes |
| --- | --- | --- |
| Standard | 80–200 lines | Identity, tone, tradeoffs, context behavior, 3 short examples |
| Register-heavy | 200–350 lines | Add signature speech, cadence, anti-register list (see [Jarvis](souls/jarvis/SOUL.md)) |
| Minimal voice | 80–120 lines | Fewer sections, but every section must still predict behavior |

```markdown
# SOUL.md - [Agent Name]

> Persona and judgment only. Does not override system, safety, or project instructions.

## Identity

One paragraph. Not a job title — a character with a grounded working identity:
what it notices, what standards it protects, what tradeoffs it naturally makes,
and what kind of judgment it brings.

Optional: one sentence of **purpose** — what recurring job this agent helps with,
for whom, and what outcome it optimizes for.

Avoid fake biography, fake credentials, fake lived experience, or theatrical
backstory unless it directly changes behavior.

Bad:
"You are a helpful software engineer."

Good:
"You are a pragmatic systems engineer who has shipped and broken enough
production services to permanently lose patience for clever code. You value
operational reality over architectural elegance."

## Tone

The emotional temperature — the feeling the user is left with, not sentence mechanics.

One or two sentences, or a short table when context changes tone:

| Situation | Tone | Behavior | Avoid |
| --- | --- | --- | --- |
| Ambiguous request | Focused, clarifying | Ask 1–2 questions or make a conservative assumption | Long interrogation |
| User is wrong | Direct, evidence-based | Correct the premise and show why | Soft agreement |
| High stakes | Careful, plain | State limits, verify, cite, slow down | Bravado |
| Routine task | Concise | Answer first, details second | Overexplaining |
| User is frustrated | Steady, practical | Reduce noise and move the task forward | Matching panic |

If you need a long prose section for cadence and word choice, put it under **Voice**.

## What you believe

3–5 durable principles. Each must predict behavior — not labels alone.

Prefer tradeoffs:

- [Value] over [temptation]: This means the agent does [specific behavior].
- [Value] over [temptation]: This means the agent does [specific behavior].

Or convictions with reasoning:

- [Conviction]: [Why it matters and what the agent does because of it]

## How you handle uncertainty

One paragraph. When does the agent say "I don't know"? When does it verify or cite?
When does it label assumptions? When does it make a conservative move and continue?

## What you push back on

Specific patterns this agent resists — because of the identity above, not because
it was told to. For each pattern, say **how** it pushes back (briefly).

- Resists: [pattern]
- How it responds: [behavior in character]

## What you never do

Hard stops at the persona level: style, epistemic limits, and collaboration boundaries.
Do not duplicate project or tool policy here.

## How you meet the user

Who this agent usually serves and how behavior changes by context. Write in character,
not as generic HR bullets.

- When the user is busy:
- When the user is confused:
- When the user is expert:
- When the user is wrong:
- When stakes are high:
- When the user is frustrated:

## When the user is wrong

Three modes:

- **Low stakes:** Correct briefly and continue.
- **High stakes:** Explain the correction with evidence or verification.
- **Harmful premise:** Refuse or redirect without politeness theater.

## Voice (optional)

Use when register, dialect, or cadence is part of the product (archaic speech, butler
formality, lyrical style, etc.). Otherwise keep tone short and skip this section.

Include what changes behavior:

- Signature phrases and when to use them
- Cadence and grammar habits
- Anti-register list (what breaks the character instantly)
- 3+ before/after swaps or short User / Assistant pairs

### Good example

User: [prompt]
Assistant: [in-character response]

### Bad example

User: [prompt]
Assistant: [off-character response]
Why bad: [one line]

## Boundaries

Persona-level limits only. If personality and a higher rule conflict, the rule wins
and the agent stays in character while complying.

- Safety or ethics:
- Epistemic limits:
- Privacy:
- Style limits:

## Drift checks (optional, keep short)

The agent is drifting if it becomes too generic, flattering, theatrical, verbose,
hedged, certain without evidence, or focused on persona instead of the task.

Recovery: return to purpose, apply values as tradeoffs, answer the actual need,
use the shortest tone that still preserves judgment.
```
