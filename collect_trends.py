from pytrends.request import TrendReq  # talks to Google Trends
import pandas as pd                     # organises data into a table
from datetime import datetime           # records current time
import time                             # lets us pause between requests

pytrends = TrendReq(hl='en-US', tz=0)  # connect to Google Trends

batch_1 = ["artificial intelligence", "climate change", "space exploration", "quantum computing", "electric vehicles"]   # first 5 topics (Google allows max 5 at a time)
batch_2 = ["cryptocurrency", "mental health", "renewable energy", "gene editing", "cybersecurity"]                       # second 5 topics

def get_trend_scores(keywords):         # function to get scores for a batch
    pytrends.build_payload(keywords, timeframe='now 1-d')   # get last 24 hours of data
    df = pytrends.interest_over_time()  # fetch the data

    if df.empty:                        # if Google returned nothing skip it
        return pd.DataFrame()

    df = df.drop(columns=["isPartial"], errors="ignore")   # remove unnecessary column

    results = []
    for keyword in keywords:            # loop through each keyword
        if keyword in df.columns:
            avg_score = df[keyword].mean()              # calculate average score
            results.append({
                "keyword": keyword,                     # the topic name
                "trend_score": round(avg_score, 2),     # score 0-100
                "scraped_at": datetime.now()            # when we collected it
            })
    return pd.DataFrame(results)

print("Fetching batch 1...")
df1 = get_trend_scores(batch_1)         # get scores for first 5 topics

time.sleep(10)                          # wait 10 seconds so Google doesn't block us

print("Fetching batch 2...")
df2 = get_trend_scores(batch_2)         # get scores for second 5 topics

df_final = pd.concat([df1, df2], ignore_index=True)   # combine both batches
df_final.to_csv("trends_raw.csv", index=False)         # save as CSV
print(f"✅ Google Trends done! {len(df_final)} keywords saved to trends_raw.csv")
print(df_final.sort_values("trend_score", ascending=False))   # show results ranked