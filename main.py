from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def startup_event():
    return {"Message:": "Hello World"}