#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os
import mysql.connector
from mysql.connector import Error

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "gzd2yk"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()
api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@api.get("customer/{idx}")
def get_customer(idx: int):
    # read the data from csv file
    df = pd.read_csv("../customers.csv")
    # filter data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@api.post("/get_paylod") # push stuff to api
async def get_payload(request: Request):
    response = await request.json()
    num1 = response.get("num1")
    num2 = response.get("num2")
    sum = num1 + num2
    return {"sum":sum}
    # return await request.json()

