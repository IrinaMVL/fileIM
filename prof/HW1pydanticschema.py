from pydantic import BaseModel, Field, validator, root_validator


class ButtonPressed(BaseModel):
    payload: str
    tokens:
    type: str


