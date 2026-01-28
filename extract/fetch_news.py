import requests

api_key = "e0c5554df7dd413f81100739c5f13144"

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
