from fastapi import FastAPI

from src.dev.router import dev_router
from src.users.router import user_router
from src.hotels.router import hotel_router

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(hotel_router, prefix="/hotel", tags=["hotel"])
app.include_router(dev_router, prefix="/dev", tags=["dev"])



@app.get("/")
async def root():
    return {"message": "Hello World"}