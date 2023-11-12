from fastapi import FastAPI
from typing import Dict

from routes.category import category_router
from routes.inventory import inventory_router
from routes.product import product_router
from routes.sales import sales_router

app = FastAPI(openapi_url="/openapi.json", title="Ecommerce Backend")


@app.get("/ping", tags=["Health"])
async def read_root() -> Dict:
    return {"message": "pong"}


app.router.prefix = "/api/v1"
app.include_router(product_router, prefix="/product", tags=["Products"])
app.include_router(category_router, prefix="/category", tags=["Category"])
app.include_router(sales_router, prefix="/sales", tags=["Sales"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])
