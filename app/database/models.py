import uuid
import dotenv

from sqlmodel import SQLModel, Field
from typing import Optional

dotenv.load_dotenv()


class Products(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    image: Optional[str] = None
