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
    welcome_message = "welcome to part1. select an time to which you want to know count of events "
    return f"""
        <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>fastapi server part1</title>
    <script src="../static/index.js" defer></script>
  </head>
  <body>
    <h1>{ welcome_message }</h1>
    <form id = "form">
      <label for="hour">Choose a hour</label>
      <select id="hour">
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
        <option>6</option>
        <option>7</option>
        <option>8</option>
        <option>9</option>
        <option>10</option>
        <option>11</option>
        <option>12</option>
       </select>
      <br>

      <label for="am_pm">Choose a hour</label>
      <select id="am_pm">
        <option>AM</option>
        <option>PM</option>
      </select>
      <br>
      <input type="submit" value="check number of events on this date">

    </form>
  </body>
</html>

    """
# response_class=HTMLResponse)    
@app.get("/data",response_class = HTMLResponse)
def data(hour:int,am_pm:str):
    print("hour",hour)
    print("am_pm",am_pm)
    
    con = sqlite3.connect("/root/.local/share/EventTracker/database.db")

    cur = con.cursor()
    # assert False,"con.cursor"
    result = cur.execute("select count(*) from events")
    # assert False,"cur.execute"
    result = result.fetchone()
    # assert False,"result.fetchone"
    print("result",result,"type_of_result",type(result))
    print(list(result))
    # con.disconnect()
    # assert False,"print(result)"
    # except Exception as e:
    #     print("e",e)
    #     return str(e)
    return f"The count of events in  {hour} {am_pm} is equall to {result[0]}"
    # return "welcome to data route"
    # open database
    # count events at day from 1 hours
    
