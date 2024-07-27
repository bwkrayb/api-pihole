import os
from typing import Union
from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


@app.get("/pi-thing")
def weather_refresh():
    text_output = str(os.system("pihole -c -e"))
    #print(text_output)
    return {"blah": text_output}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
