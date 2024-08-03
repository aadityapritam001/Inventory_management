from fastapi import FastAPI
from inventory.router import inventory_app
import uvicorn 

app = FastAPI()

app.include_router(inventory_app, prefix ="/inventory")


if __name__=="__main__":
    uvicorn.run(
        "app:app",
        host="localhost",
        port=8000,
        reload=True,
    )
