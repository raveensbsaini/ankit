from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from datetime import datetime
import time
import sqlite3
start_time = time.time()
print("start_time in epoche",start_time)
print(datetime.fromtimestamp(start_time))
# assert False
app = FastAPI()
temp = Jinja2Templates(directory="templates")
@app.get("/",response_class=HTMLResponse)
def root(request:Request):
    pass_data = {"welcome_message":"welcome to part1. select an time to which you want to know count of events "}
    return temp.TemplateResponse("index.html",{"request":request,**pass_data})
@app.get("/data")
def data(hour:int,am_pm:str):
    return "welcome to data route"
    # open database
    # count events at day from 1 hours
