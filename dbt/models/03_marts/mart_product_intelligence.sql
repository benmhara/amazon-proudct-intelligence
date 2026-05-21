{{ config(materialized='table') }}

SELECT

    p.product_id,
    p.product_name,
    p.category,

    p.actual_price,
    p.discounted_price,

    p.discount_amount,

    p.rating,
    p.rating_count,

    p.popularity_score,
    p.value_score,

    CASE
        WHEN p.value_score > 50
        THEN 'High Opportunity'

        WHEN p.value_score > 20
        THEN 'Medium Opportunity'

        ELSE 'Low Opportunity'
    END AS market_opportunity

FROM {{ ref('int_product_metrics') }} p