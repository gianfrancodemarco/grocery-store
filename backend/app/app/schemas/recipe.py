from typing import List, Optional

from app.schemas.fruit import Fruit
from pydantic import BaseModel


# Shared properties
class RecipeBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    fruits: Optional[List[Fruit]] = []


# Properties to receive on Recipe creation
class RecipeCreate(RecipeBase):
    name: str
    description: str
    fruits: Optional[List[int]]

# Properties to receive on Recipe update
class RecipeUpdate(RecipeBase):
    id: int = None
    description: str
    fruits: Optional[List[int]]


# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    id: int
    name: str
    description: str
    fruits: List[Fruit] = []
    
    class Config:
        orm_mode = True


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass
