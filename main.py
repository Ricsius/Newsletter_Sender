import requests
import os
from send_email import send

api_key = os.getenv("News_API_Key")
topic = "tesla"
language = "en"
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
    "sortBy=publishedAt&"\
    f"apiKey={api_key}&"\
    f"language={language}"

request = requests.get(url)
content = request.json() 
articles = ""

for article in content["articles"][:20]:
    title = article["title"]
    description = article["description"]
    link = article["url"]

    if title is not None and description is not None:
        articles += title + "\n" + description + "\n" + link + "\n\n"

message = """\
Subject: Today's news

PythonHow newsletter:\n\n
"""

message += articles
message = message.encode('utf-8')

send(message)