# Offline E-commerce Customer Support Chatbot

## Overview
This project implements a **functional offline customer support chatbot** for an e-commerce store using **Ollama** and **Meta’s Llama 3.2 (3B)** language model.  
The chatbot demonstrates how a local LLM can handle customer queries without sending sensitive data to the cloud, while also comparing **zero-shot** and **one-shot** prompting techniques.

---

## Project Goals
- Deploy an LLM locally for customer support.
- Learn prompt engineering techniques (zero-shot vs. one-shot).
- Evaluate model performance manually using a scoring rubric.
- Ensure data privacy by keeping all processing offline.

---

## Project Structure

ecommerce-chatbot/
├── prompts/
│ ├── zero_shot_template.txt # Zero-shot prompt template
│ └── one_shot_template.txt # One-shot prompt template with one example
├── eval/
│ └── results.md # Query results & evaluation scores
├── chatbot.py # Main Python script
├── README.md # Project overview & instructions
├── setup.md # Environment setup instructions
├── report.md # Final analysis & comparison
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment (local only, not in repo)


---

## Step-by-Step Implementation

### **Step 1: Environment Setup**
1. Install Ollama: [https://ollama.com](https://ollama.com)
2. Verify installation:
   ```powershell
   ollama --version

3.Pull the Llama 3.2 model:
ollama pull llama3.2:3b

4.Create project folder and Python virtual environment:
python -m venv venv
venv\Scripts\activate

5.Install required Python libraries:
pip install requests datasets

Step 2: Data Preparation

Adapted 20 customer queries from the Ubuntu Dialogue Corpus into e-commerce scenarios.

Queries are stored in chatbot.py:

queries = [
    "How can I track my recent order?",
    "My discount code is not working at checkout.",
    "What is your return policy?",
    ...
]

Step 3: Prompt Engineering

Zero-Shot: Instructions only, no example.

One-Shot: Instructions + one example query-response pair.

Folder: prompts/
Files: zero_shot_template.txt and one_shot_template.txt

Step 4: Build the Chatbot

Python script chatbot.py:

Loads queries and prompt templates.

Sends queries to Ollama API (llama3.2:3b).

Retrieves responses for both zero-shot and one-shot prompts.

Logs results to eval/results.md.
python chatbot.py

Step 5: Evaluation & Report

Scoring Rubric:

Criterion	Score (1-5)	Description
Relevance	1–5	How well the response addresses the query
Coherence	1–5	Grammar and readability
Helpfulness	1–5	Actionable advice provided

eval/results.md contains all queries, responses, and manual scores.

report.md summarizes performance, compares zero-shot vs. one-shot, and discusses limitations.

Usage Instructions

1.Activate Python virtual environment:
venv\Scripts\activate

2.Run chatbot:
python chatbot.py

3.Open evaluation results:

eval/results.md

4.Review final analysis:

report.md
Observations

One-shot prompting generally yields more helpful, coherent, and consistent responses.

Zero-shot works but can be vague.

Llama 3.2 (3B) works well offline on CPU, though slower than cloud GPUs.

The system ensures data privacy by processing entirely locally.

Future Improvements

Multi-turn conversations with context memory.

Integration with real-time order databases.

Fine-tuning the model on company-specific FAQs for better accuracy.