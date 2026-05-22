from pydantic import BaseModel


class SyncResponseSchema(BaseModel):
    status:str
    total_processed:int
    inserted:int
