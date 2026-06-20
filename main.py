from fastapi import FastAPI , Path, Query, Body, Form, File, UploadFile, Header, Cookie, Request
from fastapi.responses import JSONResponse
from fastapi import status
# import uvicorn
from typing import Annotated
from pydantic import BaseModel , Field
from pathlib import Path as p
import aiofiles

app = FastAPI()

# file_dirctory = p("./uploads")
# file_dirctory.mkdir(exist_ok=True)

# @app.post("/upload")
# async def uploadfile(file:Annotated[UploadFile,File()],name:Annotated[str,Form()]):
#     filename = file_dirctory / file.filename

#     async with aiofiles.open(filename,"wb") as buffer:
#         await buffer.write(await file.read())

#     return {
#         "fileSize":file.size,
#         "name":name,
#         "filename":filename
#     }

# data = [
#     {
#         "title":"python for beginer",
#         "decs":"test for one data"
#     },
#     {
#         "title":"js for beginer",
#         "decs":"test for two data"
#     },
#     {
#         "title":"java for beginer",
#         "decs":"test for three data"
#     },
# ]

# inmemorylistip:list[dict[str,str]] = []
# def isratelimit(ip:str) -> bool:
#     for ipadder in inmemorylistip:
#         if ipadder["address"] == ip:
#             if ipadder["usage_count"] <= 5:
#                 return True
#             else:
#                 return False
#     inmemorylistip.append({"address":ip,"usage_count":0})
#     return False

listip:list[dict[str,str]] = []
def checkip(ip:str) -> bool:
    for i in listip:
        if i["address"] == ip:
            if i["count"] < 4 :
                return True
            else:
                return False
    listip.append({"address":ip,"count":0})
    

@app.get("/")
async def startup_event(req:Request):
    # print(req.client.host)
    # limit = isratelimit(req.client.host)
    limit = checkip(req.client.host)
    if limit:
        return JSONResponse(status_code=status.HTTP_429_TOO_MANY_REQUESTS,content={"message":"to many request"})
    
    return {"Message:": "Hello World"}
    

# @app.get("/course/desc/seo")
# async def testparamsfunc():
#     return JSONResponse(content={"message":"description test for seo"})

# @app.get("/course/{id}/{name}")
# async def pathfunction(id:int,name:str):
# # async def pathfunction(id:str,name:str):
#     return JSONResponse(status_code=200,content={"message":f"{id} and {name}"})

# @app.get('/post/{id}')
# async def testpathfunc(id:Annotated[int,Path(lt=5,description="should enter letter than 5 number")]):
#     return JSONResponse(status_code=200 , content={"post":f"{id}"})

# @app.get('/data')
# async def queryfunc (find:Annotated[list[str],Query(description="find data with filter find")] = []):
#     if find:
#         result = [item for item in data if any(i for i in find if i.lower() in item["title"].lower())]
#         return JSONResponse(content=result,status_code=200)

# class Data(BaseModel):
#     title : Annotated[str, Field(max_length=5,description="should enter title letter than 5 caracter")]
#     # decs = Annotated[str,Body()]
#     decs : str

# @app.post("/create")
# # async def createdata(newdata:Annotated[Data,Body(embed=True)]):
# async def createdata(newdata:Annotated[Data,Body()]):
#     data.append(newdata.model_dump())
#     return JSONResponse(status_code=status.HTTP_201_CREATED,content={
#         "new":newdata.model_dump(),
#         "alldata":data
#     })

# User = [
#     {"username":"amir","password":"amir"},
#     {"username":"ehsan","password":"1234"},
# ]

# class UserMain(BaseModel):
#     username:Annotated[str,Form()]
#     password:Annotated[str,Form()]

# @app.post("/login")
# async def login(user:Annotated[UserMain,Form()]):
#     for u in User:
#         if user.username.lower() == u["username"].lower() and user.password == u['password']:
#             return JSONResponse(status_code=status.HTTP_200_OK,content={
#                 'message':f"welcome to home {user.username}"
#             })
#     return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"message":"not found"})

# class clientHeader(BaseModel):
#     # postmain_token:str
#     x_test:str

# @app.get("/test")
# async def test(headers:Annotated[clientHeader,Header()]):
# # async def herderreq(headers:Annotated[str,Header()]):
#     return {
#         # "postman_token":headers.postmain_token,
#         "x_test":headers.x_test
#         # "headers":headers
#     }

# class Cookiet(BaseModel):
#     name:str
#     age:int

# @app.get("/testcookie")
# async def test(cookie:Annotated[Cookiet,Cookie()]):
#     return JSONResponse(content={
#         "name":cookie.name,
#         "age":cookie.age
#     },status_code=status.HTTP_200_OK)

# if __name__ == "__main__":
#     uvicorn.run("main:app",host="127.0.0.1",reload=True)