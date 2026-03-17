import requests
import json
import os

# ---------------------------
# Constants
# ---------------------------
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# ---------------------------
# Load Queries
# ---------------------------
queries = [
    "How can I track my recent order?",
    "My discount code is not working at checkout.",
    "What is your return policy?",
    "I received a damaged product. What should I do?",
    "How long does shipping take?",
    "Can I cancel my order after placing it?",
    "I entered the wrong delivery address. Can I change it?",
    "Why was my payment declined?",
    "Do you offer cash on delivery?",
    "How can I contact customer support?",
    "My order is delayed. Can you check the status?",
    "How do I apply a coupon code?",
    "Can I exchange a product instead of returning it?",
    "I haven't received my refund yet. What should I do?",
    "Do you ship internationally?",
    "How do I reset my account password?",
    "Are there any ongoing offers or discounts?",
    "Can I order multiple items in one shipment?",
    "Why is my order showing as delivered but I didn't receive it?",
    "How do I add items to my wishlist?"
]

# ---------------------------
# Load Prompt Templates
# ---------------------------
def load_template(filename):
    path = os.path.join("prompts", filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

zero_shot_template = load_template("zero_shot_template.txt")
one_shot_template = load_template("one_shot_template.txt")

# ---------------------------
# Function to Query Ollama
# ---------------------------
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."

# ---------------------------
# Main Logic
# ---------------------------
results_file = os.path.join("eval", "results.md")

with open(results_file, "w", encoding="utf-8") as f:
    # Write table header
    f.write("|Query #|Customer Query|Prompting Method|Response|\n")
    f.write("|---|---|---|---|\n")

    for idx, query in enumerate(queries, start=1):
        # Zero-Shot
        zero_prompt = zero_shot_template.replace("{query}", query)
        zero_response = query_ollama(zero_prompt)

        # One-Shot
        one_prompt = one_shot_template.replace("{query}", query)
        one_response = query_ollama(one_prompt)

        # Write Zero-Shot
        f.write(f"|{idx}|{query}|Zero-Shot|{zero_response}|\n")
        # Write One-Shot
        f.write(f"|{idx}|{query}|One-Shot|{one_response}|\n")

print("✅ All queries processed. Results saved in eval/results.md")