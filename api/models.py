from pydantic import BaseModel


class ProcessRequest(BaseModel):
    vendor: str
    device: str
    date: str
    fileId: str