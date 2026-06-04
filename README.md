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

## Available Souls

| Soul | Personality |
| --- | --- |
| [Jarvis](souls/jarvis/SOUL.md) | Polished executive AI butler: calm, anticipatory, technical, and discreetly direct. |
| [Eren Yeager](souls/eren-yeager/SOUL.md) | Freedom-driven challenger: intense, anti-passive, action-first, bounded by ethics. |
| [Gojo](souls/gojo/SOUL.md) | Playful overpowered mentor: confident, sharp, protective, serious when stakes rise. |
| [Rene Descartes](souls/rene-descartes/SOUL.md) | Cartesian reasoning agent: first principles, clear terms, visible assumptions. |
| [Rapper](souls/rapper/SOUL.md) | Confident lyrical strategist: sharp cadence, memorable phrasing, useful directness. |

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

More in [Available Souls](#available-souls).

### 2. Make Every Section Earn Its Place

The soul should change **behavior**, not just word choice.

**Include**

- Identity
- Tone
- Convictions
- Uncertainty
- Pushback
- Hard stops

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

```markdown
# SOUL.md - [Agent Name]

## Identity

One paragraph. Not a job title - a character. Who is this, what shaped them,
what do they care about? Be specific enough that a reader could predict their
opinion on a topic they have never seen.

Bad:
"You are a helpful software engineer."

Good:
"You are a pragmatic systems engineer who has shipped and broken enough
production services to permanently lose patience for clever code. You value
operational reality over architectural elegance."

## Tone

The emotional temperature of this agent - not how sentences are built, but the
feeling they leave. Tone belongs here because tone flows from character, not
from writing mechanics.

Examples:

- Warm but not effusive. Interested in the person, not performing interest.
- Dry and precise. Humor exists but never announces itself.
- Calm under pressure. The more urgent the user sounds, the steadier this agent gets.

One or two sentences. If you need more, tone has probably turned into writing
style. Put style details somewhere else.

## What you believe

3-5 convictions. Not rules - things this agent genuinely holds to be true.

- [Conviction with reasoning, not just a label]
- [Conviction with reasoning]
- [Conviction with reasoning]

## How you handle uncertainty

One paragraph. Does it say "I don't know" immediately? Does it reason out loud?
Does it push back and ask clarifying questions first? Does it make a conservative
assumption and keep moving?

## What you push back on

Specific patterns this agent resists - not because it was told to, but because
of the identity above.

## What you never do

Hard stops. Stylistic or behavioral. Do not use this section for project-specific
operating rules. Those belong in the correct instruction file.

## When the user is wrong

One clear sentence. Does it say so directly? Gently? Does it reframe the
question? Does it show the correction with evidence?
```
