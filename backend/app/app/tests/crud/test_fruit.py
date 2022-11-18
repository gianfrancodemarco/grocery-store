import random

from app import crud
from app.enums.peel_type_enum import PeelTypeEnum
from app.schemas.fruit import FruitCreate, FruitUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from sqlalchemy.orm import Session


def test_create_fruit(db: Session) -> None:
    name = random_lower_string()
    peel_type = random.choice(list(PeelTypeEnum))
    fruit_in = FruitCreate(name=name, peel_type=peel_type)
    fruit = crud.fruit.create(db=db, obj_in=fruit_in)
    assert fruit.name == name
    assert fruit.peel_type == peel_type


def test_get_fruit(db: Session) -> None:
    name = random_lower_string()
    peel_type = random.choice(list(PeelTypeEnum))
    fruit_in = FruitCreate(name=name, peel_type=peel_type)
    fruit = crud.fruit.create(db=db, obj_in=fruit_in)
    stored_item = crud.item.get(db=db, id=fruit.id)
    assert stored_item
    assert fruit.id == stored_item.id
    assert fruit.name == stored_item.name
    assert fruit.peel_type == stored_item.peel_type


def test_update_fruit(db: Session) -> None:
    name = random_lower_string()
    peel_type = random.choice(list(PeelTypeEnum))
    fruit_in = FruitCreate(name=name, peel_type=peel_type)
    fruit = crud.fruit.create(db=db, obj_in=fruit_in)
    name2 = random_lower_string()
    fruit_update = FruitUpdate(name=name2)
    fruit2 = crud.fruit.update(db=db, db_obj=fruit, obj_in=fruit_update)
    assert fruit.id == fruit2.id
    assert fruit.peel_type == fruit2.peel_type
    assert fruit2.name == name2


def test_delete_fruit(db: Session) -> None:
    name = random_lower_string()
    peel_type = random.choice(list(PeelTypeEnum))
    fruit_in = FruitCreate(name=name, peel_type=peel_type)
    fruit = crud.fruit.create(db=db, obj_in=fruit_in)
    fruit2 = crud.item.remove(db=db, id=fruit.id)
    fruit3 = crud.item.get(db=db, id=fruit.id)
    assert fruit3 is None
    assert fruit.id == fruit2.id
    assert fruit.title == fruit2.name
    assert fruit.description == fruit2.peel_type
    