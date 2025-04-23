import pickle
import numpy as np

with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

def check_if_spam(words, links, capital_words, spam_word_count):
    features = np.array([[words, links, capital_words, spam_word_count]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        print(f"🚨 This message is likely SPAM (probability = {probability:.2f})")
    else:
        print(f"✅ This message is NOT spam (probability = {probability:.2f})")
