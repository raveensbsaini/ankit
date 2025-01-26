from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
def get_data():
    # if date > today:
    #     return 404 "date has not come"
    return {
        "count": random.randint(0, 1000)
    }

app.mount("/", StaticFiles(directory="templates", html=True), name="static")

@app.exception_handler(404)
async def custom_404_handler(request, __):
    return FileResponse("templates/index.html")

# @app.get("/{full_path:path}")
# async def catch_all():
#     # Read file and return
#     return Path("./templates/index.html").read_text()
