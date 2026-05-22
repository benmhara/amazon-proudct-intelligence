import streamlit as st

from snowflake.snowpark.context import (
    get_active_session
)

session = get_active_session()

st.title("🤖 AI Product Analyst")

st.markdown("""
Ask questions about:
- customer complaints
- product quality
- recommendations
- sentiment trends
- hidden opportunities
""")

question = st.chat_input(
    "Ask an AI product question..."
)

def escape_sql(text: str) -> str:
    return text.replace("'", "''") if text else ""

safe_question = escape_sql(question)    

if question:

    retrieval_sql = f"""
    WITH query_embedding AS (

        SELECT
            AI_EMBED(
                'snowflake-arctic-embed-m',
                '{safe_question}'
            ) AS embedding
    )

    SELECT

        product_name,
        review_content,

        VECTOR_COSINE_SIMILARITY(
            review_embedding,
            query_embedding.embedding
        ) AS similarity_score

    FROM AMAZON_PRODUCT_INTELLIGENCE.AI.REVIEW_EMBEDDINGS,
         query_embedding

    ORDER BY similarity_score DESC

    LIMIT 5
    """

    retrieval_df = (
        session.sql(retrieval_sql)
        .to_pandas()
    )

    context = ""

    for _, row in retrieval_df.iterrows():

        context += f"""
        Product: {row['PRODUCT_NAME']}

        Review:
        {row['REVIEW_CONTENT']}

        ---
        """
        
    safe_context = escape_sql(context)    

    completion_sql = f"""
    SELECT AI_COMPLETE(
        'mistral-large2',

        CONCAT(
            'You are an AI product analyst. ',

            'Use the following reviews to answer the question. ',

            'Question: {safe_question}. ',

            'Reviews: {safe_context}'
        )
    ) AS response
    """

    response_df = (
        session.sql(completion_sql)
        .to_pandas()
    )

    ai_response = response_df.iloc[0]["RESPONSE"]

    # clean formatting
    ai_response = ai_response.replace("\\n", "\n")  # fixes double-escaped newlines
    ai_response = ai_response.strip()

    st.chat_message("user").write(question)

    st.chat_message("assistant").write(
        ai_response
    )