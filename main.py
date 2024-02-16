import requests

api_key ="0106de8847cd4e2aa147e7c51b6eb72f"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-01-16&sortBy=publishedAt&"
       "apiKey=0106de8847cd4e2aa147e7c51b6eb72f")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
       print(article["title"])
       print(article["description"])