# app/models/post_requests.py

from pydantic import BaseModel


class RUTRequest(BaseModel):
    rut: str = ""
