import requests
from send_email import send_email

api_key = "0106de8847cd4e2aa147e7c51b6eb72f"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-01-16&sortBy=publishedAt&"
       "apiKey=0106de8847cd4e2aa147e7c51b6eb72f")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
