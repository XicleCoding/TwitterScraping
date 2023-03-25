import nltk 
import csv
import os
#nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

'''
with open('text2Analyze.txt', 'r') as f:
    text = f.read()

    # Determine sentiment polarity
    sentiment = sia.polarity_scores(text)

print(sentiment.values())
'''

#Get all csv files eith filename in the current directory
CSVFilenames=[]
for  path, currentDirectory, files in os.walk(r"C:\Users\User\OneDrive - Universidade de Aveiro\Desktop\UA\Tese\TwitterScraping"):
    for file in files:
        if file.startswith("ChatGPT_"):
            with open(file, 'r+', encoding='utf8') as csvf:
                csvreader = csv.reader(csvf)
                for tweet in csvreader:
                    #print(tweet[3])
                    #Determine sentiment polarity
                    sentiment = sia.polarity_scores(tweet[3])
                    #print(sentiment['compound'])
                    if sentiment['compound'] > 0:
                        print('Positive')
                    elif sentiment['compound'] < 0:
                        print('Negative')
                    else:
                        print('Neutral')