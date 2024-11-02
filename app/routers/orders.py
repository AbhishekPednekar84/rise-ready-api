from fastapi import APIRouter, HTTPException, status
from ..database.models import Orders
from ..database.db import SessionDep
from sqlmodel import select
from typing import List
from pydantic import UUID4


router = APIRouter()


@router.get("/orders", status_code=status.HTTP_200_OK)
def get_all_products(session: SessionDep) -> List[Orders]:
    return session.exec(select(Orders)).all()


@router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: Orders, session: SessionDep) -> Orders:
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


@router.put("/orders/delivered/{order_id}", status_code=status.HTTP_201_CREATED)
async def update_delivery_status(order_id: UUID4, session: SessionDep):
    order = session.get(Orders, order_id)
    print(order)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.delivered = True
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


@router.put("/orders/payment/{order_id}", status_code=status.HTTP_201_CREATED)
async def update_payment_status(order_id: UUID4, session: SessionDep):
    order = session.get(Orders, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.paid = True
    order.delivered = True
    session.add(order)
    session.commit()
    session.refresh(order)
    return order
