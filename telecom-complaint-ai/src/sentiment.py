from textblob import TextBlob

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity < -0.1:
        return "Negative"
    elif polarity > 0.1:
        return "Positive"
    else:
        return "Neutral"
