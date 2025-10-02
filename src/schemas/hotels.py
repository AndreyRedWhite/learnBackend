from pydantic import BaseModel, Field


class HotelSchema(BaseModel):
    title: str
    location: str


class HotelSchemaPatch(BaseModel):
    title: str | None = Field(default=None),
    location: str | None = Field(default=None)