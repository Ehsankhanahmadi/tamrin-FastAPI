from fastapi import FastAPI
from fastapi.responses import JSONResponse
# import uvicorn

app = FastAPI()

@app.get("/")
async def startup_event():
    return {"Message:": "Hello World"}

@app.get("/course/desc/seo")
async def testpathfunc():
    return JSONResponse(content={"message":"description test for seo"})

@app.get("/course/{id}/{name}")
async def pathfunction(id:int,name:str):
# async def pathfunction(id:str,name:str):
    return JSONResponse(status_code=200,content={"message":f"{id} and {name}"})


# if __name__ == "__main__":
#     uvicorn.run("main:app",host="127.0.0.1",reload=True)