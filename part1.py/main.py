from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles

from datetime import datetime
import time
import sqlite3
start_time = time.time()
print("start_time in epoche",start_time)
print(datetime.fromtimestamp(start_time))
# assert False
app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
temp = Jinja2Templates(directory="templates")
@app.get("/",response_class=HTMLResponse)
def root(request:Request):
    pass_data = {"welcome_message":"welcome to part1. select an time to which you want to know count of events "}
    return temp.TemplateResponse("index.html",{"request":request,**pass_data})
@app.get("/data")
def data(hour:int,am_pm:str):
    print("hour",hour)
    print("am_pm",am_pm)
    try:
        con = sqlite3.connect("/home/raveensbsaini/.local/share/EventTracker/database.db",check_same_thread = False)
        cur = con.cursor()
        result = cur.execute("select count(*) from events")
        result = result.fetchone()
        print("result",result,"type_of_result",type(result))
        print(list(result))
    except Exception as e:
        return e
    return f"The count of events in  {hour} {am_pm} is equall to {result[0]}"
    # return "welcome to data route"
    # open database
    # count events at day from 1 hours
    
