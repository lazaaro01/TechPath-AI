from fastapi import FastAPI
from app.routes import recommend
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base, SessionLocal
from app.models.course_model import Course
import json
import os

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if not db.query(Course).first():
        path = os.path.join(os.path.dirname(__file__), "data", "courses.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                courses_data = json.load(f)
                for c in courses_data:
                    db.add(Course(**c))
                db.commit()
    db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "API de recomendação de cursos rodando 🚀"}