import requests
import os
from send_email import send

api_key = os.getenv("News_API_Key")
url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json() 
articles = ""

for article in content["articles"]:
    title = article["title"]
    description = article["description"]

    if title is not None and description is not None:
        articles += title + "\n" + description + "\n\n"

message = """\
Subject: Newsletter

PythonHow newsletter:\n\n
"""

message += articles
message = message.encode('utf-8')

send(message)