from fastapi import APIRouter, HTTPException, status
from ..database.models import Products
from ..database.db import SessionDep
from sqlmodel import select
from typing import List


router = APIRouter()


@router.get("/products", status_code=status.HTTP_200_OK)
def get_all_products(session: SessionDep) -> List[Products]:
    return session.exec(select(Products)).all()


@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: Products, session: SessionDep) -> Products:
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@router.put("/products", status_code=status.HTTP_201_CREATED)
async def update_product(product: Products, session: SessionDep) -> Products:
    product_details = session.get(Products, product.id)

    if not product_details:
        raise HTTPException(status_code=404, detail="Order not found")

    product_details.image = product.image or product_details.image
    product_details.availability = product.availability or product_details.availability
    product_details.price = product.price or product_details.price
    product_details.name = product.name or product_details.name

    session.add(product_details)
    session.commit()
    session.refresh(product_details)
    return product_details
