def merge_data(news_df, stock_df):
    stock_df['Date'] = stock_df['Date'].dt.date
    merged_df = news_df.merge(stock_df, left_on='date', right_on='Date', how='inner')
    return merged_df