#  Viral Trend Intelligence Dashboard

A real-time data pipeline that detects trending topics across News, Google Trends and HackerNews before they go viral — built with a modern cloud data stack.

##  Tech Stack
- **Python** — data collection (NewsAPI, PyTrends, HackerNews)
- **Snowflake** — cloud data warehouse
- **dbt** — data transformation and modelling
- **Power BI** — interactive dashboard

##  Architecture
Python Scripts → Snowflake (RAW) → dbt Models → Power BI Dashboard

##  Project Structure
- collect_news.py — NewsAPI scraper
- collect_trends.py — Google Trends collector
- collect_hackernews.py — HackerNews scraper
- load_to_snowflake.py — Loads data to Snowflake
- trend_analytics/ — dbt project with staging and mart models

##  Dashboard Features
- Top trending topics ranked by Viral Score
- Platform breakdown (News vs Google vs HackerNews)
- Live trend feed with filtering by platform
- Peak Viral Score KPI card

##  How to Run
1. Clone this repository
2. Install dependencies: pip install -r requirements.txt
3. Run scrapers: python collect_news.py
4. Load to Snowflake: python load_to_snowflake.py
5. Run dbt: dbt run
6. Open Power BI dashboard

##  Author
Jeevanandh Mathivanan