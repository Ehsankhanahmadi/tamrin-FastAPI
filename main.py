from fastapi import FastAPI , Path, Query, Body
from fastapi.responses import JSONResponse
from fastapi import status
# import uvicorn
from typing import Annotated
from pydantic import BaseModel , Field

app = FastAPI()

data = [
    {
        "title":"python for beginer",
        "decs":"test for one data"
    },
    {
        "title":"js for beginer",
        "decs":"test for two data"
    },
    {
        "title":"java for beginer",
        "decs":"test for three data"
    },
]

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

@app.get('/data')
async def queryfunc (find:Annotated[list[str],Query(description="find data with filter find")] = []):
    if find:
        result = [item for item in data if any(i for i in find if i.lower() in item["title"].lower())]
        return JSONResponse(content=result,status_code=200)

class Data(BaseModel):
    title : Annotated[str, Field(max_length=5,description="should enter title letter than 5 caracter")]
    # decs = Annotated[str,Body()]
    decs : str

@app.post("/create")
# async def createdata(newdata:Annotated[Data,Body(embed=True)]):
async def createdata(newdata:Annotated[Data,Body()]):
    data.append(newdata.model_dump())
    return JSONResponse(status_code=status.HTTP_201_CREATED,content={
        "new":newdata.model_dump(),
        "alldata":data
    })

# if __name__ == "__main__":
#     uvicorn.run("main:app",host="127.0.0.1",reload=True)