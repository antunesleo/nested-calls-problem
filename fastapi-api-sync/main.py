from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/delay")
def delay_endpoint():
    time.sleep(10)
    print("delayed")
    return {"message": "Delayed endpoint executed successfully"}

@app.get("/other")
def other_endpoint():
    return {"message": "success"}
