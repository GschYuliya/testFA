from fastapi import FastAPI, Query
from random import randint
import math
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about_me")
def show_about_me(a:int, b:int):

    return{
        'name' : 'Yuliya',
        'group' : 'T-323901',
        'age' : '22',
        's' : a + b
    }

@app.get("/random_number")
def show_random_number():
    return{'random_number' : randint(1,10)}

@app.get("/s_triangle")
def search_s(a:int = Query(gt=0), b:int = Query(gt=0), c:int = Query(gt=0)):
    p = (a + b + c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return{
        'S' : s
    }