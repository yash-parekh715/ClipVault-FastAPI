from fastapi import FastAPI, Depends, status, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import model
from typing import Annotated
from database import engine, Sessionlocal
from sqlalchemy.orm import Session

# Create FastAPI Instance
origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model.Base.metadata.create_all(bind=engine)


class ClipBase(BaseModel):
    id: str
    data: str


class UpdateClip(ClipBase):
    data: str


def get_db():

    # Start the Session from AppServer with Database
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# Read Clip
@app.get("/clip", status_code=status.HTTP_200_OK)
async def get_all(db: db_dependency):
    clip = db.query(model.Clip).all()


@app.delete("/delete", status_code=status.HTTP_202_ACCEPTED)
async def delete_all(db: db_dependency):
    clip = db.query(model.Clip).all()
    for i in clip:
        db.delete(i)
    db.commit()


@app.get("/clip/{clip_id}", status_code=status.HTTP_200_OK)
async def get_clip(clip_id: str, db: db_dependency):
    clip = db.query(model.Clip).filter(model.Clip.id == clip_id).first()

    if clip is None:
        raise HTTPException(status_code=404, details='Clip not Found')
    return clip

# Create Clip


@app.post("/clip", status_code=status.HTTP_201_CREATED)
async def create_clip(clip: ClipBase, db: db_dependency):
    db_clip = model.Clip(**clip.dict())
    db.add(db_clip)
    db.commit()


# Delete Clip
@app.delete("/clip/{clip_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_clip(clip_id: str, db: db_dependency):
    clip = db.query(model.Clip).filter(model.Clip.id == clip_id).first()

    if clip is None:
        raise HTTPException(status_code=404, details='Clip not Found')

    db.delete(clip)
    db.commit()
