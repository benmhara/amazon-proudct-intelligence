import streamlit as st

from snowflake.snowpark.context import (
    get_active_session
)

session = get_active_session()

st.title("🤖 AI Product Insights")

sql = """
SELECT
    product_name,
    sentiment_label,
    ai_business_flag,
    opportunity_score
FROM AMAZON_PRODUCT_INTELLIGENCE.AI.AI_PRODUCT_INSIGHTS
LIMIT 50
"""

df = session.sql(sql).to_pandas()

st.dataframe(
    df,
    use_container_width=True
)