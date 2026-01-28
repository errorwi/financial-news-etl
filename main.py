from extract.fetch_news import fetch_news
from extract.fetch_stock_prices import fetch_stock_prices
from transform.clean_news import clean_news
from transform.sentiment_analysis import add_sentiment
from transform.merge_data import merge_data
from load.load_db import load_to_db

news = fetch_news()
stock_df = fetch_stock_prices()

news_df = clean_news(news)
news_df = add_sentiment(news_df)

news_df.rename(columns={"publishedAt": "date"}, inplace=True)

final_df = merge_data(news_df, stock_df)
load_to_db(final_df)

print("ETL Pipeline executed successfully")
