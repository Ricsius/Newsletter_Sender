import requests
import os

api_key = os.getenv("News_API_Key")
url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json() 

for article in content["articles"]:
    print(article["title"])
    print(article["description"])