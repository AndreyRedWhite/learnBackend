from pydantic import BaseModel


class HotelData(BaseModel):
    title: str
    name: str
