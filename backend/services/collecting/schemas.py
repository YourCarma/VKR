from pydantic import BaseModel,  Field, constr
from datetime import date

class CreateFishes(BaseModel):
    company_id: int = Field(ge=1, default=1)
    name: str = Field(min_length=1, max_length=35)
    catalog_id: str
    locust: str

class RecievedFish(BaseModel):
    fish_id: int = Field(ge=1)
    amount: int = Field(ge=0)
    date: date

class CreateCompany(BaseModel):
    name: str = Field(min_length=1)

class CreateUse(BaseModel):
    fish_id: int = Field(ge=1)
    unit_using: int = Field(ge=0)
    volume_using: str = Field(min_length=1)
    date: date
    