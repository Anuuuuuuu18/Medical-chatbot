# AI Medical Bot

An AI-powered chatbot that provides basic medical advice, symptom checking, and answers to common health questions.  
**Note: Not for diagnosis! Always consult a healthcare professional.**

## Features

- Symptom checker: Suggests possible causes for symptoms.
- Medical FAQ: Answers common health questions.
- User-friendly web interface (Streamlit).
- Safety disclaimer.

## Tech Stack

- Python
- NLP: spaCy, HuggingFace Transformers
- Dataset: MedQuAD, Symptoma (public sources)
- Web: Streamlit

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Example Usage

- "I have a sore throat and cough. What should I do?"
- "What is diabetes?"
- "What medicine can I take for a headache?"

## Disclaimer

This bot is for informational purposes only. Always consult a healthcare professional for medical advice.
