from sqlalchemy.orm import Session
from .models import Corp, CorpName, Tag, TagName, corp_tag
from .schemas import CorpCreate, TagCreate


def get_corps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Corp).offset(skip).limit(limit).all()


def get_corp_by_name(db: Session, corp_name: str, lang_code: str):
    subquery = db.query(CorpName.corp_id).filter(CorpName.name == corp_name).subquery()
    q = db.query(Corp).join(Corp.corp_name).filter(CorpName.corp_id.in_(subquery)).filter(CorpName.lang_code == lang_code).first()
    return q


def get_corp_by_name_autocompleted(db: Session, corp_name: str, lang_code: str):
    search_str = "%{}%".format(corp_name)
    q = db.query(Corp).join(CorpName).filter(CorpName.lang_code == lang_code, CorpName.name.like(search_str)).all()
    return q


def create_corp(db: Session, corp: CorpCreate):
    db_corp = Corp(
        name=corp.name
    )

    db.add(db_corp)
    db.commit()
    id = db_corp.id
    db.refresh(db_corp)
    return f"created corp with id {id}"


def get_corp_by_tag(db: Session, tag_name: str, lang_code: str):
    subquery = db.query(TagName.tag_id).filter(TagName.name == tag_name).subquery()
    q = db.query(Corp).join(corp_tag).filter(corp_tag.c.tag_id.in_(subquery)).filter(CorpName.lang_code == lang_code).all()
    return q


def get_tags(db: Session, skip: int = 0, limit: int = 100):
    q = db.query(Tag).join(TagName).filter(TagName.tag_id == Tag.id).offset(skip).limit(limit).all()
    return q

def create_tags(db: Session, tag: TagCreate):
    db_tag = Tag(
        name=tag.name
    )

    db.add(db_tag)
    db.commit()
    id = db_tag.id
    db.refresh(db_tag)
    return f"created tag with id {id}"

