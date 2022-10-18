from fastapi import FastAPI, File, UploadFile, Response, Request, Body
from fastapi.middleware.cors import CORSMiddleware
import subprocess


app = FastAPI()

origins = [
    "https://github.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/x1243")
async def main(payload: dict = Body(...)):
    update = f'tmux send-keys -t GitAccess "git pull" ENTER'
    subprocess.call([update], shell=True)
    return 0
