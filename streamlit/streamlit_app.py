import streamlit as st


st.set_page_config(
    page_title="Amazon Product Intelligence",
    page_icon="🧠",
    layout="wide"
)

st.title(
    "🧠 Amazon Product Intelligence Platform"
)

st.markdown("""
Welcome to the AI-powered product intelligence platform.

This application combines:

- Snowflake
- dbt
- Cortex AI
- Semantic Search
- Recommendation Systems
- Product Intelligence Analytics
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="AI Features",
        value="6"
    )

with col2:

    st.metric(
        label="Architecture",
        value="Medallion + dbt"
    )

with col3:

    st.metric(
        label="Search",
        value="Semantic"
    )

st.divider()

st.subheader("🚀 Platform Capabilities")

st.markdown("""
### 🔎 Semantic Search
Search products using meaning-based AI retrieval.

### 🎯 Product Recommendations
Discover high-potential products using AI scoring.

### 📊 Executive Dashboards
Analyze pricing, sentiment, and market opportunities.

### 🤖 AI Product Analyst
Ask natural-language questions about products and reviews.
""")

st.info(
    "Use the sidebar to explore the platform."
)