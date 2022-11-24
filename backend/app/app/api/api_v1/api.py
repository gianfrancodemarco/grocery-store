from app.api.api_v1.endpoints import (allergies, fruits, items, login, lots,
                                      users, recipes, sensors, notifications, sensor_fruit_analysis, utils)
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(fruits.router, prefix="/fruits", tags=["fruits"])
api_router.include_router(lots.router, prefix="/lots", tags=["lots"])
api_router.include_router(allergies.router, prefix="/allergies", tags=["allergies"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(sensor_fruit_analysis.router, prefix="/analysiss", tags=["analysiss"])