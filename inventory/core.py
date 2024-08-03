import sqlalchemy
from fastapi import HTTPException
from inventory.models import inventory

async def insert_inventory_data(db, inventory_data):
    try:
        new_inventory =  inventory(
            id = inventory_data.id,
            name = inventory_data.name,
            item_code = inventory_data.item_code,
            quantity = inventory_data.quantity,
            rate = inventory_data.rate,
            cost_price = inventory_data.cost_price,
            description = inventory_data.description,
            is_available = inventory_data.is_available
        )
        db.add(new_inventory)
        db.commit()

    except sqlalchemy.exc.IntegrityError:
       db.rollback()
       raise HTTPException(
           status_code = 409,
           detail = "inventory already exist !"
       )

    except Exception as ex:
        db.rollback()
        raise HTTPException(
           status_code = 409,
           detail = f"Error in inserting new inventory: {ex}"
       )
    
    else:
        return new_inventory
        

async def get_inventory_list(db):
    return db.query(inventory).all()