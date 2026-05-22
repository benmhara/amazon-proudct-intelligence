from fastapi import APIRouter

from app.database import get_connection

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/top-products")
def get_top_products():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
        SELECT
            product_name,
            category,
            rating,
            popularity_score
        FROM GOLD.BUSINESS_READY_PRODUCTS
        ORDER BY popularity_score DESC
        LIMIT 10
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    results = []

    for row in rows:

        results.append({
            "product_name": row[0],
            "category": row[1],
            "rating": row[2],
            "popularity_score": row[3]
        })

    cursor.close()
    conn.close()

    return results