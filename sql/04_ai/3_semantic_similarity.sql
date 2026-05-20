USE DATABASE amazon_product_intelligence;
USE SCHEMA ai;

CREATE OR REPLACE VIEW similar_product_reviews AS
SELECT

    a.product_name AS source_product,
    b.product_name AS similar_product,

    VECTOR_COSINE_SIMILARITY(
        a.review_embedding,
        b.review_embedding
    ) AS similarity_score

FROM review_embeddings a
JOIN review_embeddings b
    ON a.product_id != b.product_id

WHERE similarity_score > 0.85;