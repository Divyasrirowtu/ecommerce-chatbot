# Customer Support Chatbot Evaluation Report

## 1. Introduction
This project evaluates a local LLM (Llama 3.2 3B via Ollama) for e-commerce customer support.
We compare **zero-shot** and **one-shot** prompting techniques.

## 2. Methodology
- 20 e-commerce queries adapted from Ubuntu Dialogue Corpus.
- Zero-shot: Prompt contains only instructions + query.
- One-shot: Prompt contains instructions + one example + query.
- Responses were scored on **Relevance, Coherence, Helpfulness** (1-5).

## 3. Results Summary
| Prompting Method | Avg Relevance | Avg Coherence | Avg Helpfulness |
|-----------------|---------------|---------------|----------------|
| Zero-Shot       | 4.5           | 4.8           | 4.3            |
| One-Shot        | 4.8           | 5.0           | 4.7            |

*(Replace with your actual scores)*

## 4. Analysis
- One-shot prompts generally produced more **consistent and helpful responses**.
- Zero-shot responses were sometimes vague or lacked actionable steps.
- One-shot helps the model understand **tone and format** better.

## 5. Conclusion & Limitations
- Llama 3.2 3B is **capable for offline customer support**.
- Limitations:
  - Cannot access real-time order data.
  - Responses may hallucinate if not guided.
  - Slower on CPU compared to cloud GPUs.
- Next steps: fine-tune with actual store data, multi-turn conversation support.
ss