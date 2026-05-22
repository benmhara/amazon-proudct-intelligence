import streamlit as st
import pandas as pd

from snowflake.snowpark.context import (
    get_active_session
)

session = get_active_session()

st.title("🔎 Semantic Product Search")

query_text = st.text_input(
    "Search semantically"
)

if query_text:

    sql = f"""
    WITH query_embedding AS (

        SELECT
            AI_EMBED(
                'snowflake-arctic-embed-m',
                '{query_text}'
            ) AS embedding
    )

    SELECT

        product_name,
        category,
        review_content,

        VECTOR_COSINE_SIMILARITY(
            review_embedding,
            query_embedding.embedding
        ) AS similarity_score

    FROM AMAZON_PRODUCT_INTELLIGENCE.AI.REVIEW_EMBEDDINGS,
         query_embedding

    ORDER BY similarity_score DESC

    LIMIT 10
    """

    df = session.sql(sql).to_pandas()

    st.dataframe(
        df,
        use_container_width=True
    )