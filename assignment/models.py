from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base


corp_tag = Table(
    "corp_tag",
    Base.metadata,
    Column("corp_id", ForeignKey("corp.id")),
    Column("tag_id", ForeignKey("tag.id")),
)

class Corp(Base):
    __tablename__ = "corp"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    corp_name = relationship("CorpName", backref="corp")
    tags = relationship("Tag", secondary=corp_tag)

class CorpName(Base):
    __tablename__ = "corp_name"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    lang_code = Column(String)
    corp_id = Column(Integer, ForeignKey("corp.id"))


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    tag_names = relationship("TagName", cascade="all,delete", backref="tag")

class TagName(Base):
    __tablename__ = "tag_name"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    lang_code = Column(String)
    tag_id = Column(Integer, ForeignKey("tag.id"))


