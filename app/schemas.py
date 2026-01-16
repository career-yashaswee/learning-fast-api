from pydantic import BaseModel, Field

from app.database.models import ShipmentStatus

class Book(BaseModel):
    title: str
    weight: float = Field(le=25)
    status: str
    content: str