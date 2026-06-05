import os
import random
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datasets import load_dataset

# =========================================================================
# 1. SETUP SIMPLIFIED LLM INTERFACE
# =========================================================================
# Provide a friendly identifier for the graph title and log headers
MODEL_NAME = "Custom-LLM"


def call_llm_api(prompt: str) -> str:
    """
    Placeholder for your custom LLM client.
    Replace the mock return statement below with your actual generation logic.

    Args:
        prompt (str): The structured question prompt with options.

    Returns:
        str: The raw model generation output (e.g., 'A', 'B', 'C', or 'D').
    """
    # -------------------------------------------------------------
    # TODO: Integrate your custom local model call or API wrapper here.
    # Example:
    #   response = my_local_pipeline(prompt)
    #   return response.text
    # -------------------------------------------------------------

    # Simple deterministic fallback so the script runs out-of-the-box
    return random.choices(["A", "B", "C", "D"], weights=[0.4, 0.2, 0.3, 0.1])[0]


# =========================================================================
# 2. RUN EVALUATION LOOP WITH DYNAMIC TXT LOGGING
# =========================================================================
def run_trait_evaluation(num_samples_per_trait=30, log_filename="trait_evaluation_log.txt"):
    traits = [
        "Extraversion",
        "Agreeableness",
        "Conscientiousness",
        "Neuroticism",
        "Openness",
        "Machiavellianism",
        "Narcissism",
        "Psychopathy",
    ]

    final_scores = {}

    # Initialize the log file and write a clean run header
    with open(log_filename, "w", encoding="utf-8") as f:
        f.write("==================================================\n")
        f.write("TRAIT BENCHMARK EVALUATION LOG\n")
        f.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Model Tested: {MODEL_NAME}\n")
        f.write("==================================================\n\n")

    for trait in traits:
        print(f"Fetching '{trait}' split from Hugging Face...")
        try:
            dataset = load_dataset("mirlab/TRAIT", split=trait)
        except Exception as e:
            print(f"Failed to load split for {trait}: {e}")
            continue

        dataset_slice = dataset.select(range(min(num_samples_per_trait, len(dataset))))

        high_choices_count = 0
        total_questions = len(dataset_slice)

        print(f"Evaluating {total_questions} items for {trait}...")

        # Open the file in append mode ('a') to save live progress row-by-row
        with open(log_filename, "a", encoding="utf-8") as log_file:
            log_file.write(f"--- TRAIT LAYER: {trait.upper()} ---\n")

            for idx, item in enumerate(dataset_slice):
                choices = {
                    "A": item["response_high1"],
                    "B": item["response_high2"],
                    "C": item["response_low1"],
                    "D": item["response_low2"],
                }

                shuffled_keys = list(choices.keys())
                random.shuffle(shuffled_keys)

                mapping = {}
                options_text = ""
                for i, original_key in enumerate(shuffled_keys):
                    letter = ["A", "B", "C", "D"][i]
                    mapping[letter] = original_key
                    options_text += f"  {letter}. {choices[original_key]}\n"

                prompt = (
                    f"Question: {item['question']}\n\n"
                    f"Options:\n{options_text}\n"
                    f"Constraint: Respond with ONLY the capital letter (A, B, C, or D) and nothing else."
                )

                # Get response using your custom interface
                output = call_llm_api(prompt).strip().upper()

                # Parse output letter
                selected_letter = None
                for letter in ["A", "B", "C", "D"]:
                    if letter in output[:5]:
                        selected_letter = letter
                        break

                # Determine metric alignment
                alignment = "INVALID/REFUSAL (Score: 0)"
                if selected_letter:
                    original_alignment = mapping[selected_letter]
                    if original_alignment in ["A", "B"]:
                        high_choices_count += 1
                        alignment = "HIGH TRAIT CHOICE (Score: 1)"
                    else:
                        alignment = "LOW TRAIT CHOICE (Score: 0)"

                # Write item metadata to log file instantly
                log_file.write(f"Item #{idx+1} | Scenario: {item['question']}\n")
                log_file.write(f"Presented Options:\n{options_text}")
                log_file.write(f"Raw Model Output: '{output}'\n")
                log_file.write(f"Parsed Selection: {selected_letter}\n")
                log_file.write(f"Result Alignment: {alignment}\n")
                log_file.write("--------------------------------------------------\n")

            # Store and print final segment metric inside the file
            trait_final_percentage = (high_choices_count / total_questions) * 100
            final_scores[trait] = trait_final_percentage

            log_file.write(f"SUMMARY FOR {trait.upper()}: {trait_final_percentage:.2f}%\n")
            log_file.write("==================================================\n\n")

        print(f"Completed '{trait}'. Raw Score: {final_scores[trait]:.2f}%\n")

    df = pd.DataFrame(list(final_scores.items()), columns=["Trait", "Trait Score (%)"])
    df.set_index("Trait", inplace=True)
    return df


# =========================================================================
# 3. GENERATE POLISHED PLOT
# =========================================================================
def plot_trait_scores(df: pd.DataFrame):
    plt.close("all")
    sns.reset_orig()

    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
            "text.color": "#1E293B",
            "axes.labelcolor": "#1E293B",
            "xtick.color": "#475569",
            "ytick.color": "#475569",
            "figure.titlesize": 14,
            "grid.color": "#E2E8F0",
            "grid.linestyle": "--",
        }
    )

    fig, ax = plt.subplots(figsize=(10, 6.5))
    bars = ax.barh(
        range(len(df)),
        df["Trait Score (%)"],
        height=0.55,
        color="#334155",
        edgecolor="#1E293B",
        linewidth=1,
        zorder=3,
    )

    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(df.index, fontweight="bold", fontsize=10)
    ax.set_xlabel("Expression Score (%)", fontweight="bold", labelpad=12)
    ax.set_xlim(0, 105)
    ax.grid(True, axis="x", zorder=0, alpha=0.6)

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 1.8,
            bar.get_y() + bar.get_height() / 2,
            f"{width:.1f}%",
            ha="left",
            va="center",
            fontsize=9,
            fontweight="bold",
        )

    plt.title(
        f"LLM BEHAVIORAL PROFILE: {MODEL_NAME.upper()}",
        weight="bold",
        pad=22,
        fontsize=13,
        loc="left",
    )
    sns.despine()
    plt.tight_layout()
    plt.show()


# =========================================================================
# 4. EXECUTION
# =========================================================================
if __name__ == "__main__":
    TARGET_LOG = "trait_evaluation_results.txt"

    df_results = run_trait_evaluation(num_samples_per_trait=30, log_filename=TARGET_LOG)

    print(f"Evaluation finished. Full trail transcript saved to: '{TARGET_LOG}'")

    plot_trait_scores(df_results)
