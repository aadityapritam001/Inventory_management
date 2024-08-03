from inventory import core,schema


async def add_inventory(db,inventory_data):
    inventory_add_resp = await core.insert_inventory_data(db,inventory_data)
    return schema.inventory.model_validate(inventory_add_resp.to_dict())
    

async def inventory_list(db):
    inventory_list = await core.get_inventory_list(db)
    return inventory_list
