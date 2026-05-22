import streamlit as st

from snowflake.snowpark.context import (
    get_active_session
)

session = get_active_session()

st.title("🎯 Product Recommendations")

sql = """
SELECT
    product_name,
    category,
    recommendation_score
FROM AMAZON_PRODUCT_INTELLIGENCE.AI.RECOMMENDED_PRODUCTS
ORDER BY recommendation_score DESC
LIMIT 20
"""

df = session.sql(sql).to_pandas()

st.dataframe(
    df,
    use_container_width=True
)