from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Header, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from assignment.database import SessionLocal, engine
from assignment import models, crud, schemas


app = FastAPI(
    title="WantedLab Assignment",
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/corps/", response_model=list[schemas.Corp], tags=["Companies"])
def read_corps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    corps = crud.get_corps(db, skip=skip, limit=limit)
    return corps


@app.get("/corp/{corp_name}", response_model=schemas.Corp, tags=["Companies"])
def corp_search(corp_name: str, x_wanted_language: str = Header(), db: Session = Depends(get_db)):
    lang_code = 'ko'
    if x_wanted_language:
        lang_code = x_wanted_language
    corp = crud.get_corp_by_name(db, corp_name=corp_name, lang_code=lang_code)
    if corp is None:
        raise HTTPException(status_code=404, detail="검색 결과가 없습니다")
    return corp


@app.get("/search", response_model=list[schemas.Corp], tags=["Companies"])
def corp_name_autocomplete(query: str, x_wanted_language: str = Header(), db: Session = Depends(get_db)):
    lang_code = 'ko'
    if x_wanted_language:
        lang_code = x_wanted_language
    corp = crud.get_corp_by_name_autocompleted(db, corp_name=query, lang_code=lang_code)
    return JSONResponse(content=jsonable_encoder(corp))


@app.post("/corp", status_code=status.HTTP_201_CREATED, tags=["Companies"])
def create_corp(corp: schemas.CorpCreate, db: Session = Depends(get_db)):
    corp = crud.create_corp(db, corp=corp)
    return corp


@app.get("/tags", response_model=list[schemas.Corp], tags=["Tags"])
def read_corp_by_tag(query: str, x_wanted_language: str = Header(), db: Session = Depends(get_db)):
    if x_wanted_language:
        lang_code = x_wanted_language
    corp = crud.get_corp_by_tag(db, tag_name=query, lang_code=lang_code)
    return corp


