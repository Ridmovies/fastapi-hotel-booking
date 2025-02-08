from fastapi import FastAPI

from src.dev.router import dev_router

app = FastAPI()
app.include_router(dev_router, prefix="/dev", tags=["dev"])

@app.get("/")
async def root():
    return {"message": "Hello World"}