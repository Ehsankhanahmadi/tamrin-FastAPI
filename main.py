from fastapi import FastAPI , Path
from fastapi.responses import JSONResponse
# import uvicorn
from typing import Annotated

app = FastAPI()

@app.get("/")
async def startup_event():
    return {"Message:": "Hello World"}

@app.get("/course/desc/seo")
async def testparamsfunc():
    return JSONResponse(content={"message":"description test for seo"})

@app.get("/course/{id}/{name}")
async def pathfunction(id:int,name:str):
# async def pathfunction(id:str,name:str):
    return JSONResponse(status_code=200,content={"message":f"{id} and {name}"})

@app.get('/post/{id}')
async def testpathfunc(id:Annotated[int,Path(lt=5,description="should enter letter than 5 number")]):
    return JSONResponse(status_code=200 , content={"post":f"{id}"})

# if __name__ == "__main__":
#     uvicorn.run("main:app",host="127.0.0.1",reload=True)