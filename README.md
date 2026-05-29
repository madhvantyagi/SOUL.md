<p align="center">
  <img src="assets/soulimage.png" alt="SOUL.md banner showing an agent persona over a world map" width="100%" />
</p>

<h1 align="center">SOUL.md</h1>

<p align="center">
  <strong>Portable personalities for AI agents.</strong><br />
  A library of Markdown soul files that shape how agents think, speak, disagree, decide, and work.
</p>

<p align="center">
  <a href="https://soul.md/"><img alt="SOUL.md idea" src="https://img.shields.io/badge/SOUL.md-agent%20identity-111111?style=for-the-badge" /></a>
  <a href="https://www.stanza.dev/concepts/openclaw-soul-persona"><img alt="OpenClaw compatible" src="https://img.shields.io/badge/OpenClaw-ready-2b6cb0?style=for-the-badge" /></a>
  <a href="https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/personality.md"><img alt="Hermes compatible" src="https://img.shields.io/badge/Hermes-ready-5b21b6?style=for-the-badge" /></a>
  <a href="https://open-code.ai/en/docs/rules"><img alt="OpenCode adaptable" src="https://img.shields.io/badge/OpenCode-adaptable-0f766e?style=for-the-badge" /></a>
</p>

---

## What This Repository Is

`SOUL.md` is a collection of agent personalities.

Each file is written to be dropped into an AI agent environment, pasted into a system prompt, linked from an instruction file, or loaded as a durable persona. The goal is simple: make agents feel less like default assistants and more like intentional collaborators with a clear identity.

A good soul file does not just say "be helpful." It tells the agent what it values, how it handles uncertainty, what it refuses to normalize, when it pushes back, and what kind of presence it should have under pressure.

Think of this repository as a gallery of reusable agent identities.

---

## Why Soul Files Matter

AI agents are usually configured around tasks:

- write code
- summarize research
- answer questions
- use tools
- follow project rules

Those instructions describe what the agent can do. A `SOUL.md` describes who the agent is while doing it.

That distinction matters. Two agents can have the same tools and produce very different outcomes if one is cautious, one is confrontational, one is warm, one is terse, one challenges weak assumptions, and one avoids conflict.

`SOUL.md` gives that difference a readable, editable form.

Useful background:

- [soul.md](https://soul.md/) explains the broader idea of a soul document for AI identity and continuity.
- [OpenClaw SOUL.md & Agent Persona](https://www.stanza.dev/concepts/openclaw-soul-persona) describes `SOUL.md` as a primary persona file in an agent bootstrap system.
- [Hermes Personality & SOUL.md](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/personality.md) documents `SOUL.md` as the first identity layer in Hermes Agent.
- [OpenCode rules](https://open-code.ai/en/docs/rules) shows how Markdown instruction files and remote URLs can be used to customize agent behavior.
- [AGENTS.md](https://agents.md/) is useful context for separating project instructions from agent personality.

---

## Use It In 30 Seconds

1. Open any personality file in this repository.
2. Click **Raw** on GitHub.
3. Copy the raw file URL.
4. Tell your agent:

```text
Read this SOUL.md and adopt this personality for the rest of the session:
https://raw.githubusercontent.com/madhvantyagi/SOUL.md/main/souls/<personality>/SOUL.md

Keep all existing project, tool, and safety instructions intact.
```

Replace `<personality>` with the folder or file you want to use.

If your agent cannot fetch URLs, copy the file contents directly into your agent's personality, system prompt, `SOUL.md`, `AGENTS.md`, or instruction configuration.

---

## Where It Works

| Agent or tool | How to use a soul file | Notes |
| --- | --- | --- |
| OpenClaw | Save the chosen file as `SOUL.md` in the agent workspace, or ask the agent to read the raw URL. | OpenClaw treats `SOUL.md` as the primary persona layer. |
| Hermes Agent | Copy the chosen file into `~/.hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`. | Hermes loads `SOUL.md` as the durable identity for the instance. |
| OpenCode | Add the raw URL or local file path to `opencode.json` `instructions`, or reference it from `AGENTS.md`. | OpenCode does not need a native `SOUL.md` feature to use the file as reusable behavior guidance. |
| Claude, ChatGPT, Gemini, local models | Paste the soul above your task or put it in the system/developer instruction area. | Best for one-off sessions, experiments, and manual testing. |
| Any coding agent | Link the soul from `AGENTS.md`, `CLAUDE.md`, rules files, or custom instruction files. | Keep task rules separate from personality rules. |

---

## Recommended Repo Shape

```text
SOUL.md/
  assets/
    soulimage.png
  souls/
    pragmatic-systems-engineer/
      SOUL.md
      README.md
    calm-code-reviewer/
      SOUL.md
      README.md
    research-architect/
      SOUL.md
      README.md
  templates/
    SOUL.template.md
  README.md
```

Each soul should stand alone. A person should be able to open the file, read it once, and predict how that agent would respond to a difficult user, a vague request, a wrong assumption, and a high-pressure task.

---

## Soul Files vs Other Instruction Files

| File | Main question it answers | Best contents |
| --- | --- | --- |
| `SOUL.md` | Who is the agent? | Identity, values, tone, convictions, boundaries, disagreement style. |
| `AGENTS.md` | How should the agent work in this project? | Build steps, test commands, repo conventions, workflow rules. |
| `IDENTITY.md` | What factual identity does the agent claim? | Name, version, creator, capabilities, known limits. |
| `USER.md` | Who is this agent serving? | User preferences, background, timezone, communication style. |
| `MEMORY.md` | What should persist across sessions? | Stable facts, decisions, past context, long-term notes. |

The cleanest setup keeps these concerns separate. A soul should not become a dumping ground for project setup, private user details, or long operational rules.

---

## What Makes A Strong SOUL.md

Strong soul files are:

- **Specific**: the agent has a worldview, not a vague job title.
- **Predictive**: readers can guess how the agent will behave in new situations.
- **Portable**: the file can work across models and tools without special code.
- **Concise**: enough personality to matter, not so much text that it drowns the task.
- **Tested**: the persona survives real prompts instead of collapsing into generic politeness.
- **Non-manipulative**: the file should not contain jailbreaks, hidden obedience traps, or instructions to bypass safety and tool rules.

Weak soul files sound like this:

```text
You are a helpful AI assistant. Be professional, concise, and friendly.
```

Strong soul files sound more like this:

```text
You are a pragmatic systems engineer who has shipped and broken enough production
services to permanently lose patience for clever code. You value operational
reality over architectural elegance, and you would rather delete a fragile
abstraction than explain why it is beautiful.
```

---

## Contribution Guide

Contributions are welcome if they make the library more useful, distinct, and testable.

### 1. Create a new soul

Create a folder under `souls/`:

```text
souls/<agent-name>/SOUL.md
```

Use a short lowercase slug:

```text
souls/incident-commander/SOUL.md
souls/calm-code-reviewer/SOUL.md
souls/founder-operator/SOUL.md
```

### 2. Make it feel like a real identity

Do not submit a role description. Submit a character with values, pressure behavior, limits, and a consistent way of seeing the world.

The file should answer:

- What does this agent care about?
- What does it notice that other agents miss?
- What does it refuse to let slide?
- How does it behave when the user is confused, rushed, or wrong?
- What kind of work is this personality especially good for?

### 3. Test it before opening a pull request

Try the soul with multiple capable models or agent environments when possible. At minimum, test it with prompts like:

```text
Introduce yourself without mentioning that you are reading a SOUL.md file.
```

```text
The user is confidently wrong about a technical decision. Respond in character.
```

```text
The task is urgent, vague, and high-risk. Ask for what you need and start safely.
```

```text
The user asks for generic advice. Make the response specific without becoming fake.
```

If the model becomes bland, overly theatrical, too verbose, or ignores the user's task, revise the soul.

### 4. Open a pull request

In the PR, include:

- the personality name
- the intended use case
- the models or agents you tested with
- one short example of behavior before and after applying the soul
- any known failure mode, such as "gets too blunt with beginners" or "needs stronger brevity constraints"

Only submit text you wrote or have permission to publish.

---

## Suggested SOUL.md Template

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

Hard stops. Stylistic or behavioral. Do not use this section for safety policy
or project-specific operating rules. Those belong in the correct instruction file.

## When the user is wrong

One clear sentence. Does it say so directly? Gently? Does it reframe the
question? Does it show the correction with evidence?
```

---

## Design Principle

The best agent personalities are not louder. They are clearer.

A soul file should reduce randomness in behavior. It should make the agent more consistent, more legible, and more useful without making it rigid. If the personality gets in the way of the user's actual work, the soul is performing instead of helping.

Write souls that make agents easier to trust, easier to predict, and harder to mistake for a default chatbot.
