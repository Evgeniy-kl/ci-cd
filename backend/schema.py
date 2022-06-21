from pydantic import BaseModel


class UserItem(BaseModel):
    email: str
    password: str
    is_active: bool

    class Config:
        orm_mode = True
