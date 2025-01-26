from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
import sqlite3
import json
app = FastAPI()


@app.get("/",response_class = HTMLResponse)
def root():
    welcome_message = "welcome to part1. select an time to which you want to know count of events "
    javascript_code = """
        document.addEventListener("DOMContentLoaded",function (){
            let form_ele = document.querySelector("#form")
            form_ele.onsubmit = function (event){
                event.preventDefault()
                let hour_ele = document.querySelector("#hour")
                let hour = hour_ele.value
                let am_pm_ele = document.querySelector("#am_pm")
                let am_pm = am_pm_ele.value
                let url = new URL(window.location.href)
                url.pathname = "/data"
                url.searchParams.append("hour",hour)
                url.searchParams.append("am_pm",am_pm)
                url = url.toString()
                result = fetch(url)
                result.then(response =>{
                console.log(response)
                return response.json()})
                .then(data =>{
                para_ele = document.querySelector("#para")
                data = JSON.parse(data)
                console.log("in last",data,typeof(data),data.hour,data.am_pm,data.counts)
                para_ele.innerHTML  = `Total click in ${data.hour}, ${data.am_pm} is ${data.counts}`
                console.log(data)
                }
                )
                
           
            };

        });
        
    """
    return f"""
        <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>fastapi server part1</title>
    <script>{ javascript_code }</script>
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
        <p id="para"></p>
  </body>
</html>

    """

    
@app.get("/data")
def data(hour,am_pm):
    con = sqlite3.connect("/root/.local/share/EventTracker/database.db")  
    cur = con.cursor()
    result = cur.execute("select count(*) from events")
    result  = list(result.fetchone())
    print(result)
    return_dict =  {"hour":hour,"am_pm":am_pm,"counts":result[0]}
    print(return_dict)
    return_json = json.dumps(return_dict)
    print(type(return_json))
    return return_json
