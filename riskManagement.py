import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# example text
text = input("Enter the text you want to analyze: ")

# example stock levels
stock_levels = input("Enter the stock levels (comma separated): ")
stock_levels = [int(level.strip()) for level in stock_levels.split(",")]
average_stock_level = sum(stock_levels) / len(stock_levels)

# combine text and stock level data
text_with_stock_info = f"Stock levels are at {average_stock_level}. {text}"

# analyze sentiment of text with stock info
sentiment_scores = sia.polarity_scores(text_with_stock_info)

# print sentiment scores
print(sentiment_scores)
