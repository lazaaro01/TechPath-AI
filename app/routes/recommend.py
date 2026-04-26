from fastapi import APIRouter
from app.models.user_profile import UserProfile
from app.services.recommendation_service import recomendar_curso
from app.services.groq_service import gerar_explicacao

router = APIRouter()

@router.post("/recomendar")
def recomendar(perfil: UserProfile):
    curso = recomendar_curso(perfil)
    explicacao = gerar_explicacao(curso, perfil)

    return {
        "curso_recomendado": curso,
        "explicacao": explicacao
    }