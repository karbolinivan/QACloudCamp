from pydantic import BaseModel, Field
from utils.fakers import Generator


class Resource(BaseModel):
    id: int
    title: str
    body: str
    userId: int


class CreateResource(BaseModel):
    title: str = Field(default=Generator().get_title())
    body: str = Field(default=Generator().get_body())
    userId: int = Field(default=Generator().get_userid())
