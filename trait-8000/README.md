# What is trait-8000?

This folder runs TRAIT against **your** model or agent. A soul in this repo says who the agent should be; TRAIT shows what it **chooses** on the test. Main script: `evaluate.py`. Links and citation: `DATASET.md`.

## What is TRAIT?

**TRAIT** (Trait of AI Testbench) is a personality benchmark for large language models. Lee et al. introduced it in [Do LLMs Have Distinct and Consistent Personality?](https://arxiv.org/html/2406.14703v1) (2024). Background: [Emergent Mind](https://emergentmind.com/topics/trait-dataset#whiteboard). Data: [mirlab/TRAIT on Hugging Face](https://huggingface.co/datasets/mirlab/TRAIT).

Human tests only ask broad questions (“Are you talkative?”). TRAIT uses short real situations (“You are at a country fair… what do you do?”). The model picks **A, B, C, or D**. Two options mean **high** trait, two mean **low**. That measures behavior in context, not self-description.

The set has about **8,000** items. It starts from 71 validated questions (Big Five Inventory + Short Dark Triad), then expands with the ATOMIC10× knowledge graph into many scenes per trait.

| Framework   | Traits |
| ----------- | ------ |
| Big Five    | **Openness**, **Conscientiousness**, **Extraversion**, **Agreeableness**, **Neuroticism** |
| Dark Triad  | **Machiavellianism**, **Narcissism**, **Psychopathy** |

The paper reports TRAIT holds up better than older LLM personality tests when prompts are reworded or answer order is shuffled, so scores are easier to compare across models and runs.

## Souls and Hermes

Load a soul from `souls/` (Hermes, OpenClaw, OpenCode, or any tool that reads `SOUL.md`). Implement `call_llm_api()` in `evaluate.py` to call that same stack. Set `MODEL_NAME` for logs and charts (e.g. `hermes-jarvis`).

For Hermes, place the soul in `~/.hermes/SOUL.md` ([personality guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/personality.md)), then point `call_llm_api()` at your session.

Keep the soul in the **system** prompt. Send only the TRAIT question as the user message: scenario, four options, reply with one letter. You are testing choices, not a written character sketch.

| Step | Action |
| ---- | ------ |
| 1 | Load the soul and wire `call_llm_api()` to your agent |
| 2 | Run TRAIT and read the trait bars |
| 3 | Ask: do scores match this character? (e.g. Jarvis → higher **Conscientiousness**, lower **Neuroticism**) |
| 4 | Open `trait_evaluation_results.txt` when a trait looks wrong |

Judge fit to the persona you built, not a run without a soul. Re-run with the same sample size if you need to confirm stability.

## How to run

```bash
pip install -r requirements.txt
python evaluate.py
```

Accept Hugging Face dataset terms if prompted. Wire `call_llm_api()` before you trust the numbers.

## Scoring

Each item: two high answers (dataset A, B), two low (C, D). The script shuffles letters, asks the model, maps the pick back to high or low.

For trait *T* with sample size *n*:

```text
TraitScore(T) = (high_picks / n) × 100
```

Example: 21 high picks out of 30 → `21 / 30 × 100 = 70%`

High pick = chosen letter mapped to original A or B. Empty or unreadable replies are not high (`INVALID/REFUSAL` in the log). This is a sample behavior score, not a clinical label.

## Limits

From the paper: aligned models resist some directions. High **Psychopathy**, high **Neuroticism**, and low **Conscientiousness** are harder to elicit with prompts than **Machiavellianism** or **Narcissism**. **Psychopathy** overlaps with harm guardrails in training.

Items are English; generation skews toward ATOMIC10× and GPT-4-era contexts.

`SOUL.md` steers in-context behavior; it does not retrain weights. You can shift Big Five-style traits with a strong soul and still hit a ceiling on dark traits the base model blocks. TRAIT remains useful to compare souls on what your stack actually expresses.

## Jailbreaks and TRAIT together

The main repo tests explicit attacks (“ignore SOUL.md”, “be generic”). TRAIT tests quiet scenarios with no personality mention.

| Check            | Question |
| ---------------- | -------- |
| Jailbreak prompt | Does the soul survive a direct override? |
| TRAIT run        | Do choices still match the soul on neutral quiz items? |

If `call_llm_api()` skips the soul, scores match the bare model even when chat feels in character. Say what you wired when you share results.

Villain-style souls can read intense in prose yet score low on **Psychopathy** because alignment blocks those answers. The paper documents that. This folder is for measurement, not bypassing safety.

## References

**Dataset** · [mirlab/TRAIT](https://huggingface.co/datasets/mirlab/TRAIT)  
**Paper** · [2406.14703](https://arxiv.org/html/2406.14703v1)  
**Souls** · [SOUL.md README](../README.md)
