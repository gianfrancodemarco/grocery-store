from app import crud, schemas
from app.core.config import settings
from app.enums.peel_type_enum import PeelTypeEnum
from app.enums.fruit_size_enum import FruitSizeEnum
from app.enums.recipe_budget_enum import RecipeBudgetEnum
from sqlalchemy.orm import Session

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    fruits_in = [
        schemas.FruitCreate(
            name="Pear",
            peel_type=PeelTypeEnum.EDIBLE.value
        ),
        schemas.FruitCreate(
            name="Banana",
            peel_type=PeelTypeEnum.NOT_EDIBLE.value
        ),
        schemas.FruitCreate(
            name="Apple",
            peel_type=PeelTypeEnum.NOT_EDIBLE.value
        ),
        schemas.FruitCreate(
            name="Melon",
            peel_type=PeelTypeEnum.NOT_EDIBLE.value,
            size=FruitSizeEnum.BIG.value
        ),
        schemas.FruitCreate(
            name="Orange",
            peel_type=PeelTypeEnum.NOT_EDIBLE.value
        ),
        schemas.FruitCreate(
            name="Cranberry",
            peel_type=PeelTypeEnum.EDIBLE.value,
            size=FruitSizeEnum.LITTLE.value
        )
    ]

    for fruit_in in fruits_in:
        fruit = crud.fruit.get_by_name(db, name=fruit_in.name)
        if not fruit:
            crud.fruit.create(
                db, obj_in=fruit_in
            )

    lots_in = [
        schemas.LotCreate(
            name="Test Lot n.1 of Oranges",
            timestamp_arrival="2022-10-25 12:10:01",
            weight="2.5",
            volume="3.4",
            fruit_id=crud.fruit.get_by_name(db, name='Orange').id
        ),
        schemas.LotCreate(
            name="Test Lot n.2",
            fruit_id=crud.fruit.get_by_name(db, name='Cranberry').id
        )
    ]
        
    for lot_in in lots_in:
        lot = crud.lot.get_by_name(db, name=lot_in.name)
        if not lot:
            crud.lot.create(
                db, obj_in=lot_in
            )

    allergy = crud.allergy.get_by_name(db, name="Grass pollen")
    if not allergy:
        crud.allergy.create(
            db, 
            obj_in=schemas.AllergyCreate(
                name="Grass pollen", 
                symptoms="itching or tingling in the mouth",
                fruits=[crud.fruit.get_by_name(db, name='Orange').id, crud.fruit.get_by_name(db, name='Melon').id]
                )
            )

    allergy = crud.allergy.get_by_name(db, name="Ragweed pollen")
    if not allergy:
        crud.allergy.create(
            db, 
            obj_in=schemas.AllergyCreate(
                name="Ragweed pollen", 
                symptoms="lightheadedness",
                fruits=[crud.fruit.get_by_name(db, name='Banana').id, crud.fruit.get_by_name(db, name='Melon').id]
                )
            )

    recipe = crud.recipe.get_by_name(db, name="Spiced Pear Old-Fashioned")
    if not recipe:
        crud.recipe.create(
            db, 
            obj_in=schemas.RecipeCreate(
                name="Spiced Pear Old-Fashioned", 
                description="""This old-fashioned with rosemary and pear is the perfect fall cocktail.
                    If you can't find cardamom bitters, 
                    you can use orange or Angostura bitters instead and add a pinch of ground cardamom.""",
                fruits=[crud.fruit.get_by_name(db, name='Pear').id]
                )
            )

    recipe = crud.recipe.get_by_name(db, name="Apple-Cranberry Crostada")
    if not recipe:
        crud.recipe.create(
            db, 
            obj_in=schemas.RecipeCreate(
                name="Apple-Cranberry Crostada", 
                description="""While a good pie crust ought to be a part of every cook's repertoire, sometimes there just isn't the time. 
                    But why leave the baking to the grocery stores or bakery when puff pastry is a simple,
                    high-quality stand-in for the original? In this Crostada, 
                    the sheet dough is baked free-form with ingredients piled on top. Couldn't be easier!
                    """,
                fruits=[crud.fruit.get_by_name(db, name='Apple').id, crud.fruit.get_by_name(db, name='Cranberry').id],
                budget=RecipeBudgetEnum.LOW.value
                )
            )

    sensor = crud.sensor.get_by_name(db, name="GTX42")
    if not sensor:
        crud.sensor.create(
            db,
            obj_in=schemas.SensorCreate(
                name="GTX42",
                fruit_size=FruitSizeEnum.BIG.value
            )
        )