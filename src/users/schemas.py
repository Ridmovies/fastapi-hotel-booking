from pydantic import BaseModel


class UserSchemaBase(BaseModel):
    username: str
    email: str | None = None


class UserSchemaCreate(UserSchemaBase):
    hashed_password: str


class UserSchema(UserSchemaBase):
    id: int
