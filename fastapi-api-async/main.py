from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/delay")
async def delay_endpoint():
    await asyncio.sleep(10)
    print("delayed")
    return {"message": "Delayed endpoint executed successfully"}

@app.get("/other")
async def other_endpoint():
    return {"message": "success"}
