from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    email: EmailStr
    password: str
    username: str


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    username: str
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]
