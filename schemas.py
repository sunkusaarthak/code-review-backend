from pydantic import BaseModel

class CodeModel(BaseModel):
    code: str

class OutputModel(BaseModel):
    output: str