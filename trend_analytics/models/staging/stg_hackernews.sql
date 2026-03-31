SELECT
    title,
    score,
    scraped_at
FROM {{ source('raw', 'raw_hackernews') }}
WHERE title IS NOT NULL
AND score > 0