from typing import List, Optional

from app.schemas.fruit import Fruit
from pydantic import BaseModel


# Shared properties
class AllergyBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    symptoms: Optional[str] = None
    fruits: Optional[List[Fruit]] = []


# Properties to receive on Allergy creation
class AllergyCreate(AllergyBase):
    name: str
    symptoms: str
    fruits: Optional[List[int]]

# Properties to receive on Allergy update
class AllergyUpdate(AllergyBase):
    id: int = None
    symptoms: str
    fruits: Optional[List[int]]


# Properties shared by models stored in DB
class AllergyInDBBase(AllergyBase):
    id: int
    name: str
    symptoms: str
    fruits: List[Fruit] = []
    
    class Config:
        orm_mode = True


# Properties to return to client
class Allergy(AllergyInDBBase):
    pass


# Properties properties stored in DB
class AllergyInDB(AllergyInDBBase):
    pass
