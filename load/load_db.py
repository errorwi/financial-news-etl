import mysql.connector

def load_to_db(df):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="0range69",
        database="financial_news"
    )
    cursor=conn.cursor()


    for _, row in df.iterrows():
        cursor.execute("INSERT INTO news_stock_data (date, title, description, sentiment) VALUES (%s, %s, %s, %s)",
                       (row["date"], row["title"], row["description"], row["sentiment"]))
    conn.commit()
    conn.close()