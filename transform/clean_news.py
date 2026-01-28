import pandas as pd

def clean_news(articles):
    df = pd.DataFrame(articles)
    df = df[["title", "description", "publishedAt"]]
    df.dropna(inplace=True)
    df["publishedAt"] = pd.to_datetime(df["publishedAt"]).dt.date
    return df
    