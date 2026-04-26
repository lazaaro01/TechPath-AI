from fastapi import APIRouter
from pydantic import BaseModel
from app.models.user_profile import UserProfile
from app.services.recommendation_service import recomendar_curso
from app.services.groq_service import gerar_explicacao, extrair_perfil, gerar_roadmap

router = APIRouter()

class ChatInput(BaseModel):
    message: str

@router.post("/recomendar")
def recomendar(perfil: UserProfile):
    curso_obj = recomendar_curso(perfil)
    explicacao = gerar_explicacao(curso_obj["nome"], perfil)
    roadmap = gerar_roadmap(curso_obj["nome"], perfil)

    return {
        "curso_recomendado": curso_obj,
        "explicacao": explicacao,
        "roadmap": roadmap
    }

@router.post("/recomendar_texto")
def recomendar_texto(chat_input: ChatInput):
    dados_perfil = extrair_perfil(chat_input.message)
    perfil = UserProfile(**dados_perfil)
    
    curso_obj = recomendar_curso(perfil)
    
    explicacao = gerar_explicacao(curso_obj["nome"], perfil)
    roadmap = gerar_roadmap(curso_obj["nome"], perfil)

    return {
        "perfil_identificado": dados_perfil,
        "curso_recomendado": curso_obj,
        "explicacao": explicacao,
        "roadmap": roadmap
    }