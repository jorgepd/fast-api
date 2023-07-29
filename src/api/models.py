# imports
from pydantic import BaseModel



class MessageRequest(BaseModel):
    msg: str


class MessageModel(MessageRequest):
    id: int

