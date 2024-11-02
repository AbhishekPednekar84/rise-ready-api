from fastapi import APIRouter, HTTPException, status
from ..database.models import OrderWindow
from ..database.db import SessionDep
from sqlmodel import select


router = APIRouter()


@router.get("/order_window/{day_of_week}", status_code=status.HTTP_200_OK)
async def get_order_window(day_of_week: str, session: SessionDep):
    print(day_of_week)
    window = session.exec(
        select(OrderWindow).where(OrderWindow.day_of_week == day_of_week)
    )

    if not window:
        raise HTTPException(status_code=404, detail="Order window does not exist")
    else:
        return True


@router.post("/order_window", status_code=status.HTTP_201_CREATED)
async def create_order_window(
    order_window: OrderWindow, session: SessionDep
) -> OrderWindow:
    session.add(order_window)
    session.commit()
    session.refresh(order_window)
    return order_window
