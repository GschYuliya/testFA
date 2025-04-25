from fastapi import FastAPI, Query
from random import randint
import math
import pyd
app = FastAPI()

items=[{
    'id':1,
    'name':'Toster',
    'price': 10,
    'description': 'dfsfsf',
},
{
    'id':2,
    'name':'Poste',
    'price': 100,
    'description': 'dfsf',
},
{
    'id':3,
    'name':'ggoste',
    'price': 111,
    'description': 'dfsf',
},
{
    'id':4,
    'name':'Te',
    'price': 110,
    'description': 'd',
}
]

#@app.get("/")
#def read_root():
#    return {"Hello": "World"}

#@app.get("/about_me")
#def show_about_me(a:int, b:int):

 #   return{
#      'name' : 'Yuliya',
#        'group' : 'T-323901',
#        'age' : '22',
#        's' : a + b
#    }

#@app.get("/random_number")
#def show_random_number():
#    return{'random_number' : randint(1,10)}

#@app.get("/s_triangle")
#def search_s(a:int = Query(gt=0), b:int = Query(gt=0), c:int = Query(gt=0)):
#    p = (a + b + c)/2
#    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#    return{
#        'S' : s
 #   }

@app.get('/items')
def get_items(name:str | None=Query(None,min_length=2),
            min_price:int | None=Query(None,gt=0),
            max_price:int | None=Query(None,gt=0),
            limit:int=Query(10,lt=100)):
    if max_price and min_price:
        if max_price < min_price:
            raise HTTPException(400, "Price min than max")
    k = []
    for i in items:
        if name:
            if name != i['name']:
                continue
        if min_price:
            if min_price > i['price']:
                continue
        if max_price:
            if max_price < i['price']:
                continue
        k.append(i)
    return k[:limit]

@app.get('/items/{item_id}')
def get_items_id(item_id:int=Path(gt=0)):
    for i in items:
        if i['id']==item_id:
            return i
    raise HTTPException(400, "not found")

@app.post('/items/', response_model=pyd.Item)
def post_items(item:pyd.Item):
    item=dict(item)
    id = items[-1]['id'] + 1
    item['id'] = id
    items.append(item)
    return item
