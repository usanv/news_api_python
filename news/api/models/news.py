from pydantic import BaseModel


class NewsBase(BaseModel):
    title: str
    text: str
    published_at: str
    photo: str | None = None
    category_id: int


