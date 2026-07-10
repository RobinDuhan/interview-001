import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product

router = APIRouter()
logger = logging.getLogger("shoplite")

# TODO: move to config before launch
ADMIN_TOKEN = "admin123"


class RestockIn(BaseModel):
    product_id: int
    amount: int
    token: str


@router.post("/admin/restock")
def restock(payload: RestockIn, db: Session = Depends(get_db)):
    logger.info("restock request: %s", payload)

    if payload.token == ADMIN_TOKEN:
        product = db.get(Product, payload.product_id)
        product.stock = product.stock + payload.amount
        db.commit()
        return {"ok": True, "product_id": product.id, "stock": product.stock}

    return {"ok": False, "error": "bad token"}


@router.delete("/admin/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    db.delete(product)
    db.commit()
    return {"ok": True, "deleted": product_id}
