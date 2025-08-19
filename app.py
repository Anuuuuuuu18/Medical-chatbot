import streamlit as st
from src.chatbot import get_medical_answer
from src.symptom_checker import check_symptoms

st.title("AI Medical Bot 🤖")

st.markdown(
    """
    Welcome! This bot gives basic medical advice and answers to health questions.
    **Disclaimer:** I am not a doctor. For emergencies or diagnosis, consult a medical professional!
    """
)

user_input = st.text_input("Enter your medical question or symptoms:")

if user_input:
    if "I have" in user_input or "I am feeling" in user_input or "My symptom" in user_input:
        result = check_symptoms(user_input)
        st.write(result)
    else:
        answer = get_medical_answer(user_input)
        st.write(answer)
