import pandas as pd

FAQ_PATH = "data/medical_faq.csv"

def get_medical_answer(user_query):
    # Dummy implementation: just look up the FAQ
    df = pd.read_csv(FAQ_PATH)
    for i, row in df.iterrows():
        if row["question"].lower() in user_query.lower():
            return row["answer"]
    return "Sorry, I don't have information about that. Please consult a healthcare professional."
