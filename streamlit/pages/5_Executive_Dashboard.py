import streamlit as st

from snowflake.snowpark.context import (
    get_active_session
)

session = get_active_session()

st.title("📊 Executive Dashboard")

sql = """
SELECT
    category,
    COUNT(*) AS total_products,
    AVG(rating) AS avg_rating,
    AVG(discount_percentage) AS avg_discount
FROM AMAZON_PRODUCT_INTELLIGENCE.GOLD.BUSINESS_READY_PRODUCTS
GROUP BY category
ORDER BY total_products DESC
"""

df = session.sql(sql).to_pandas()

st.bar_chart(
    df.set_index("CATEGORY")["TOTAL_PRODUCTS"]
)

st.dataframe(
    df,
    use_container_width=True
)