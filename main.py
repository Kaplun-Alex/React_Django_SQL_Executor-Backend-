from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import json

app = FastAPI(openapi_url="/api/v1/openapi.json")

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/rsql"
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/sqls/{item_id}")
async def read_item(item_id: str, sql: Union[str, None] = None):
    print(sql)
    cursor.execute(sql)
    item = cursor.fetchall()
    for i in item:
        print(i)
    return {"data": item}
