from typing import Union
from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


# sample list in python
sample_list = [{"name": "item1", "description": "item1 description", "price": 100, "tax": 10}, { "name": "item2", "description": "item2 description", "price": 200, "tax": 20}, { "name": "item3", "description": "item3 description", "price": 300, "tax": 30}, { "name": "item4", "description": "item4 description", "price": 400, "tax": 40}, { "name": "item5", "description": "item5 description", "price": 500, "tax": 50}, { "name": "item6", "description": "item6 description", "price": 600, "tax": 60}, { "name": "item7", "description": "item7 description", "price": 700, "tax": 70}, { "name": "item8", "description": "item8 description", "price": 800, "tax": 80}, { "name": "item9", "description": "item9 description", "price": 900, "tax": 90}, { "name": "item10", "description": "item10 description", "price": 1000, "tax": 100}]



class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None







@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge = 0, le=1000)],
    q: str | None= None,
    item: Item | None = None
    ):
    result = {"item_id": item_id}

 
    result.update({"sample_list": sample_list})
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item})
    return result
   
