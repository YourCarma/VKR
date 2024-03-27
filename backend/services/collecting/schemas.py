from pydantic import BaseModel,  Field, constr
from datetime import date

class CreateSource(BaseModel):
    source_id: int = Field(ge=1, default=1)
    url: str = Field(min_length=10, max_length=100)
    politic_view: str = Field(min_length=3, max_length=15)


    