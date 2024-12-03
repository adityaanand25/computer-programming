# Detect emotions in text data for sentiment analysis.
from textblob import TextBlob
def detect_emotion(text):
    analysis = TextBlob(text)
    return analysis.sentiment
print(detect_emotion("I love programming!"))
