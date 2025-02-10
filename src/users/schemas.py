from pydantic import BaseModel


class UserSchemaBase(BaseModel):
    email: str | None = None


class UserSchemaCreate(UserSchemaBase):
    password: str


class UserSchema(UserSchemaBase):
    id: int
