SELECT
    platform,
    topic,
    viral_score,
    CURRENT_TIMESTAMP AS calculated_at
FROM {{ ref('mart_viral_score') }}
ORDER BY viral_score DESC
LIMIT 20