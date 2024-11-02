import uuid
import dotenv

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date
from pydantic import EmailStr

dotenv.load_dotenv()

TODAY = date.today().strftime("%d-%b-%Y")


class Products(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    image: Optional[str] = None
    price: float
    availability: str


class Orders(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    mobile_number: str
    email_address: Optional[EmailStr] = None
    tower: str
    apartment_number: str
    dosa_qty: Optional[float] = Field(default=0)
    idly_qty: Optional[float] = Field(default=0)
    vada_qty: Optional[float] = Field(default=0)
    ragi_qty: Optional[float] = Field(default=0)
    jowar_qty: Optional[float] = Field(default=0)
    black_rice_qty: Optional[float] = Field(default=0)
    organic_ragi_qty: Optional[float] = Field(default=0)
    organic_jowar_qty: Optional[float] = Field(default=0)
    order_date: str = Field(default=TODAY)
    order_total: float = Field(default=0)
    delivered: Optional[bool] = Field(default=False)
    paid: Optional[bool] = Field(default=False)


class OrderWindow(SQLModel, table=True):
    __tablename__ = "order_window"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    day_of_week: str
    start_time: str
    end_time: str
