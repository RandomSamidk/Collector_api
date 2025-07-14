from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    event_type: str
    event_time: int
    user_id: int
    product_id: str

class Context(BaseModel):
    browser: str
    version: str
    device: str

class DataObj(BaseModel):
    events:List[Event]
    ctx: Context