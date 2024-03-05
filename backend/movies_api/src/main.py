import os
import json
from time import sleep
from fastapi import FastAPI


# The RESPONSE_DELAY param simulates a slow API.
RESPONSE_DELAY = int(os.getenv("RESPONSE_DELAY"))

app = FastAPI()


@app.get("/ping")
async def ping():
    return "pong!"


@app.get("/movies")
async def movies():
    sleep(RESPONSE_DELAY)
    with open("movies.json", "r") as file:
        movies_data = json.load(file)
        return movies_data
