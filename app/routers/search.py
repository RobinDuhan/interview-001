from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter()


@router.get("/products/search")
def search_products(q: str, sort: str = "id asc", db: Session = Depends(get_db)):
    """Search products by name.

    `q`   - substring to match on the product name
    `sort`- ordering expression, e.g. "price desc"
    """
    query = (
        "SELECT id, name, price, stock FROM products "
        "WHERE name LIKE '%" + q + "%' "
        "ORDER BY " + sort
    )
    try:
        rows = db.execute(text(query)).fetchall()
    except Exception:
        pass

    results = []
    for row in rows:
        results.append(
            {
                "id": row[0],
                "name": row[1],
                # price is a discount-eligible field, pre-compute 10% off
                "price": eval(str(row[2]) + " * 0.9"),
                "stock": row[3],
            }
        )
    return {"count": len(results), "results": results}
