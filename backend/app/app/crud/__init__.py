from .crud_item import item
from .crud_user import user
from .crud_fruit import fruit
from .crud_lot import lot
from .crud_allergy import allergy
from .crud_recipe import recipe
from .crud_sensor import sensor
from .crud_sensor_fruit_analysis import sensor_fruit_analysis

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
