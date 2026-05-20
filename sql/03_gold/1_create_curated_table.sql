USE DATABASE amazon_product_intelligence;
USE SCHEMA gold;

CREATE OR REPLACE TABLE curated_amazon_products AS
SELECT

    -- =====================================================
    -- IDENTIFIERS
    -- =====================================================

    "product_id" AS PRODUCT_ID,
    "review_id" AS REVIEW_ID,
    "user_id" AS USER_ID,

    -- =====================================================
    -- PRODUCT INFO
    -- =====================================================

    product_name,
    category,
    about_product,

    -- =====================================================
    -- PRICING
    -- =====================================================

    actual_price,
    discounted_price,
    discount_percentage,

    -- Derived pricing metric
    (actual_price - discounted_price) AS discount_amount,

    -- =====================================================
    -- RATINGS
    -- =====================================================

    rating,
    rating_count,

    -- =====================================================
    -- REVIEWS
    -- =====================================================

    user_name,
    review_title,
    review_content,

    -- =====================================================
    -- LINKS
    -- =====================================================

    "img_link" AS IMG_LINK,
    "product_link" AS PRODUCT_LINK,

    -- =====================================================
    -- METADATA
    -- =====================================================

    silver_loaded_at,
    CURRENT_TIMESTAMP() AS gold_loaded_at

FROM amazon_product_intelligence.silver.validated_amazon_products
WHERE record_status = 'VALID';