import streamlit as st
import pandas as pd

from snowflake.snowpark.context import (
    get_active_session
)

session = get_active_session()

st.title("🏆 Top Products")

query = """
SELECT
    product_name,
    category,
    rating,
    popularity_score
FROM AMAZON_PRODUCT_INTELLIGENCE.GOLD.BUSINESS_READY_PRODUCTS
ORDER BY popularity_score DESC
LIMIT 20
"""

df = session.sql(query).to_pandas()

st.dataframe(
    df,
    use_container_width=True
)