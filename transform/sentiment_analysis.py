from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def add_sentiment(df):
    df['sentiment'] = df['description'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    return df