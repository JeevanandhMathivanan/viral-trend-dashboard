WITH news AS (
    SELECT
        title AS topic,
        'NEWS'                        AS platform,
        50                            AS viral_score
    FROM {{ ref('stg_news_articles') }}
),

trends AS (
    SELECT
        keyword                       AS topic,
        'GOOGLE TRENDS'               AS platform,
        ROUND(trend_score, 2)         AS viral_score
    FROM {{ ref('stg_google_trends') }}
),

hackernews AS (
    SELECT
        title                         AS topic,
        'HACKERNEWS'                  AS platform,
        LEAST(ROUND(score * 2, 2), 100) AS viral_score
    FROM {{ ref('stg_hackernews') }}
)

SELECT * FROM news
UNION ALL
SELECT * FROM trends
UNION ALL
SELECT * FROM hackernews
ORDER BY viral_score DESC