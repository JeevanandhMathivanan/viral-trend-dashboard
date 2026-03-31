import pandas as pd                                        # reads our CSV files
import snowflake.connector                                 # connects Python to Snowflake
from snowflake.connector.pandas_tools import write_pandas  # pushes dataframe into Snowflake table

conn = snowflake.connector.connect(
    user="Jeevanandh",      # my Snowflake login username
    password="JeevanandhMathi1",  # my Snowflake login password
    account="wfmzmva-xs82593",   
    warehouse="COMPUTE_WH",              # default warehouse — already exists
    database="TREND_DB",                 # database we created in Stage 1
    schema="RAW"                         # schema where our raw tables live
)
print("✅ Connected to Snowflake!")

df_news = pd.read_csv("news_raw.csv")              # read news CSV
df_news.columns = df_news.columns.str.upper()      # Snowflake needs uppercase column names
write_pandas(conn, df_news, "RAW_NEWS_ARTICLES")   # push into Snowflake table
print(f"✅ Loaded {len(df_news)} news articles into Snowflake!")

df_trends = pd.read_csv("trends_raw.csv")          # read trends CSV
df_trends.columns = df_trends.columns.str.upper()  # uppercase columns
write_pandas(conn, df_trends, "RAW_GOOGLE_TRENDS") # push into Snowflake table
print(f"✅ Loaded {len(df_trends)} trend scores into Snowflake!")

df_hn = pd.read_csv("hackernews_raw.csv")          # read hackernews CSV
df_hn.columns = df_hn.columns.str.upper()          # uppercase columns
write_pandas(conn, df_hn, "RAW_HACKERNEWS")        # push into Snowflake table
print(f"✅ Loaded {len(df_hn)} HackerNews stories into Snowflake!")

conn.close()                                        # close the connection cleanly
print("\n All data loaded into Snowflake successfully!")


