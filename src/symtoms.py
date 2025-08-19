def check_symptoms(text):
    # Very basic keyword-based symptom checker for demo
    symptoms = {
        "cough": "Possible cold, flu, or allergy. If severe or with fever, consult a doctor.",
        "fever": "Monitor your temperature. If above 102°F (39°C), seek medical advice.",
        "headache": "Could be caused by stress, dehydration, or infection. Drink water and rest.",
        "sore throat": "Could be viral or bacterial. If it lasts more than 3 days, see a doctor.",
    }
    for symptom, advice in symptoms.items():
        if symptom in text.lower():
            return advice
    return "Symptoms not recognized. Please provide more details or consult a healthcare professional."
