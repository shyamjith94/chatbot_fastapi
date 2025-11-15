from typing import Optional
from src.api.schema import CommonRequestSchema, CommonResponseSchema
from src.core import BlogUseCaseEnum


class Blog(CommonRequestSchema):
    title:str
    content:str
    
class BlogBase(CommonRequestSchema):
    topic:str
    use_case:str = BlogUseCaseEnum.GENERATE_BLOG.value
    language:str = "english"

class BlogRequest(BlogBase, CommonRequestSchema):
    pass

class BlogResponse(BlogBase,CommonResponseSchema):
    blog:Blog