from fastapi import FastAPI, Depends
from . import schema, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request: schema.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog