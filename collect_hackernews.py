import requests                        # makes web calls
import pandas as pd                    # organises data into a table
from datetime import datetime          # records current time

print("Fetching story IDs from HackerNews...")
url = "https://hacker-news.firebaseio.com/v0/newstories.json"   # free public API — no key needed
response = requests.get(url)           # call the API
story_ids = response.json()[:50]       # grab first 50 story IDs only

stories = []                           # empty list — fills up as we loop

for i, story_id in enumerate(story_ids):   # loop through each story ID
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"   # each story has its own URL
    story = requests.get(story_url).json()                                       # get story details

    if story and story.get("type") == "story":   # only include actual stories (not comments or jobs)
        stories.append({
            "title": story.get("title", ""),     # headline of the story
            "score": story.get("score", 0),      # upvote score on HackerNews
            "scraped_at": datetime.now()         # when we collected it
        })

    if i % 10 == 0:                              # print progress every 10 stories
        print(f"  Fetched {i}/50 stories...")

df = pd.DataFrame(stories)                       # convert list into a table
df.to_csv("hackernews_raw.csv", index=False)     # save as CSV
print(f"✅ HackerNews done! {len(df)} stories saved to hackernews_raw.csv")
print(df.sort_values("score", ascending=False).head(5))   # show top 5 stories