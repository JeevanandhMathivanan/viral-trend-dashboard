SELECT
    keyword,
    trend_score,
    scraped_at
FROM {{ source('raw', 'raw_google_trends') }}
WHERE trend_score > 0