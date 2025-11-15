

from typing import Annotated, List, TypedDict
from pydantic import BaseModel, Field
from langgraph.graph import add_messages

class Blog(BaseModel):
    title:str = Field(description="Title of the blog post")
    content:str = Field(description="Content of the blog post")


class BlogState(TypedDict):
    topic:str
    blog:Blog
    language:str
    use_case:str