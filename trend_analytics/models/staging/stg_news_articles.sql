SELECT
    title,
    subreddit AS category,
    created_utc,
    scraped_at
FROM {{ source('raw', 'raw_news_articles') }}
WHERE title IS NOT NULL