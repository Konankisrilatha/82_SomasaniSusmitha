from flask import Flask, render_template, request, jsonify
import pandas as pd

from src.predict import classify_complaint
from src.sentiment import get_sentiment
from ai_services.translate import translate_to_english
from db import get_db

app = Flask(__name__)

# =========================
# DATASET PATHS
# =========================
TRAINING_DATASET_PATH = "data/customer interactionData.csv"
TICKET_DATASET_PATH = "data/customer_support_tickets.csv"

# Load ticket dataset for simulation
ticket_df = pd.read_csv(TICKET_DATASET_PATH)

def assign_priority(category, sentiment):
    if sentiment == "Negative" and category.lower() == "network":
        return "High"
    elif sentiment == "Negative":
        return "Medium"
    else:
        return "Low"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    complaint = request.form["complaint"]

    translated_text, detected_lang = translate_to_english(complaint)

    category = classify_complaint(translated_text)
    sentiment = get_sentiment(translated_text)
    priority = assign_priority(category, sentiment)

    simulated_ticket_id = len(ticket_df) + 1

    db = get_db()
    db.execute(
        "INSERT INTO tickets (complaint, category, sentiment, priority) VALUES (?,?,?,?)",
        (translated_text, category, sentiment, priority)
    )
    db.commit()

    return jsonify({
        "ticket_id": simulated_ticket_id,
        "language": detected_lang,
        "category": category,
        "sentiment": sentiment,
        "priority": priority
    })

if __name__ == "__main__":
    app.run(debug=True)
