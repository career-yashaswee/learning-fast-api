from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str
    weight: float = Field(le=25)
    status: str
    content: str