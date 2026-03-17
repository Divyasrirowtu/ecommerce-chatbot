# Customer Support Chatbot Evaluation Report

## 1. Introduction
This project builds an offline chatbot using Ollama and Llama 3.2.
The goal is to compare zero-shot and one-shot prompting techniques.

## 2. Methodology
- 20 e-commerce queries were used.
- Zero-shot: instructions only.
- One-shot: instructions + 1 example.
- Evaluation based on:
  - Relevance
  - Coherence
  - Helpfulness

## 3. Results
(Write your averages here after scoring)

Example:
- Zero-Shot:
  - Relevance: 4.4
  - Coherence: 4.7
  - Helpfulness: 4.2

- One-Shot:
  - Relevance: 4.8
  - Coherence: 5.0
  - Helpfulness: 4.7

## 4. Analysis
- One-shot responses are more structured and helpful.
- Zero-shot responses sometimes lack detail.
- One-shot improves tone and consistency.

## 5. Conclusion
- Local LLM works well for basic support tasks.
- Limitations:
  - No real-time order data
  - Possible incorrect answers
- Future improvements:
  - Add database integration
  - Multi-turn conversations