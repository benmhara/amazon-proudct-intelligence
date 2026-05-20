USE DATABASE amazon_product_intelligence;
USE SCHEMA ai;

CREATE OR REPLACE TABLE review_embeddings AS
SELECT

    product_id,
    review_id,
    product_name,
    category,
    review_content,

    -- =====================================================
    -- VECTOR EMBEDDING
    -- =====================================================

    AI_EMBED(
        'snowflake-arctic-embed-m',
        review_content
    ) AS review_embedding,

    CURRENT_TIMESTAMP() AS embedding_created_at

FROM amazon_product_intelligence.gold.business_ready_products
WHERE review_content IS NOT NULL;