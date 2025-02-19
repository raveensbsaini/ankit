from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Union

app = FastAPI() 
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/",response_class = HTMLResponse)
def root():
    return index.html
