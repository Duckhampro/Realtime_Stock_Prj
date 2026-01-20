SELECT
    symbol,
    current_price,
    change_amount,
    TO_TIMESTAMP_NTZ(fetched_at) AS fetched_at,
    change_percent
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY fetched_at DESC) AS rn
    FROM {{ ref('silver_clean_stock_quotes') }}
) t
WHERE rn = 1
