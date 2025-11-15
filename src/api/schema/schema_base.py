from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass


class CommonRequestSchema(BaseSchema):
    pass

class CommonResponseSchema(BaseSchema):
    pass