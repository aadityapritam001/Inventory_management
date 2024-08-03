from fastapi import APIRouter, Depends
import asyncio
from inventory import schema
from database.db import Database
from inventory import services


inventory_app = APIRouter()
session= asyncio.run(Database.get_db())
db = session()

@inventory_app.post("/create")
async def create_inventory(inventory_details: schema.inventory):
    return await services.add_inventory(db,inventory_details) 



@inventory_app.get("/inventory_list")
async def get_all_inventory():
    return await services.inventory_list(db)