import requests

api_key = "api_key"

def fetch_news(query="stocks"):
    url = "https://newsapi.org/v2/everything"
    params ={
        "q": query,
        "language" : "en",
        "sortBy" : "publishedAt",
        "apiKey": api_key
    }

    response = requests.get(url, params = params)
    data = response.json()

    return data["articles"]
