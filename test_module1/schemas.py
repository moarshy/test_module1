# test_module_1/schemas.py
from pydantic import BaseModel

class InputSchema(BaseModel):
    message: str = "Hello"

class OutputSchema(BaseModel):
    numpy_version: str
    message: str