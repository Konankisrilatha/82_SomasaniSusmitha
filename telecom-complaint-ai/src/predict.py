import joblib
from src.preprocess import clean_text

model = joblib.load("models/classifier.pkl")
tfidf = joblib.load("models/tfidf.pkl")

def classify_complaint(text):
    cleaned = clean_text(text)
    vector = tfidf.transform([cleaned])
    return model.predict(vector)[0]
