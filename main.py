import requests
from send_email import send_email
import os

topic = "tesla"
api_key = os.getenv("firstApiKey")
url = (f"https://newsapi.org/v2/everything?q="
       f"{topic}&from=2024-01-19&sortBy=publishedAt&apiKey={api_key}"
       f"&language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["description"] is not None:
        body = ("Subject: Today's news" + "\n" + body + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2 * "\n")

body = body.encode("utf-8")
send_email(message=body)
