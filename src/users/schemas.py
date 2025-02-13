from pydantic import BaseModel, EmailStr


class UserSchemaBase(BaseModel):
    email: EmailStr | None = None


class UserSchemaCreate(UserSchemaBase):
    password: str


class UserSchema(UserSchemaBase):
    id: int
