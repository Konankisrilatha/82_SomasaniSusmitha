import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from preprocess import clean_text

TRAINING_DATASET_PATH = "../data/customerInteractionData.csv"

df = pd.read_csv(TRAINING_DATASET_PATH)

df["clean_text"] = df["CustomerInteractionRawText"].apply(clean_text)

X = df["clean_text"]
y = df["AgentAssignedTopic"]

tfidf = TfidfVectorizer()
X_vec = tfidf.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

joblib.dump(model, "../models/classifier.pkl")
joblib.dump(tfidf, "../models/tfidf.pkl")

print("✅ ML model trained successfully")
