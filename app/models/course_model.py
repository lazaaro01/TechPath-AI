from sqlalchemy import Column, String, JSON
from app.core.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(String, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    salario_medio = Column(String)
    skills = Column(JSON)
    dificuldade = Column(String)
    duracao = Column(String)
    tags = Column(JSON)
