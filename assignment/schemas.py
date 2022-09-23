from typing import List, Optional
from pydantic import BaseModel


class TagNameBase(BaseModel):
    id: int
    name: str


class TagNameCreate(TagNameBase):
    name: str
    lang_code: str
    tag_id: int


class TagName(TagNameBase):
    lang_code: str
    tag_id: int
    class Config:
        orm_mode = True


class TagBase(BaseModel):
    id: int
    name: str


class TagCreate(BaseModel):
    name: str
    tag_names: List[TagName] = []


class Tag(TagBase):
    tag_names: List[TagName] = []

    class Config:
        orm_mode = True


class TagSummary(TagBase):
    class Config:
        orm_mode = True


class CorpBase(BaseModel):
    id: int
    name: str


class CorpCreate(BaseModel):
    name: str


class Corp(CorpBase):
    tags: List[TagSummary] = []

    class Config:
        orm_mode = True
