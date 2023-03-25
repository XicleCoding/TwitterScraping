import nltk 
#nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

with open('text2Analyze.txt', 'r') as f:
    text = f.read()

    # Determine sentiment polarity
    sentiment = sia.polarity_scores(text)

print(sentiment.values())