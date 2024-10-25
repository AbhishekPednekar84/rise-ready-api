import dotenv

dotenv.load_dotenv()

import uuid
import os


from sqlmodel import SQLModel, create_engine, Field


class Products(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    image: str

DATABSE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABSE_URI)
