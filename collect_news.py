import requests                        # lets Python make web calls to APIs
import pandas as pd                    # organises data into a table
from datetime import datetime          # lets us record the current time

API_KEY = "9f960f7491fe45c3bbf53a02b727685f"   # My personal NewsAPI key

topics = ["artificial intelligence", "technology", "climate change", "cryptocurrency", "space"]   # topics to search for

all_articles = []                      # empty list — we fill this up as we loop

for topic in topics:                   # go through each topic one by one
    url = (f"https://newsapi.org/v2/everything?q={topic}&sortBy=popularity&pageSize=20&language=en&apiKey={API_KEY}")   # build the request URL for this topic
    response = requests.get(url)       # send the request to NewsAPI
    data = response.json()             # convert the response into readable Python data

    if data["status"] == "ok":         # only continue if the request worked
        for article in data["articles"]:              # loop through each article returned
            all_articles.append({
                "title": article["title"],            # headline of the article
                "subreddit": topic,                   # which topic this article belongs to
                "upvotes": 0,                         # not used for news — set to 0
                "upvote_ratio": 0,                    # not used for news — set to 0
                "comments": 0,                        # not used for news — set to 0
                "created_utc": article["publishedAt"],# when the article was published
                "scraped_at": datetime.now()          # when WE collected it
            })
        print(f"✅ {topic}: {len(data['articles'])} articles collected")   # confirm how many collected

df = pd.DataFrame(all_articles)        # convert list into a table
df.to_csv("news_raw.csv", index=False) # save table as CSV file on your computer
print(f"\n Total: {len(df)} articles saved to news_raw.csv")   # final confirmation