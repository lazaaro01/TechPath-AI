from app.core.database import SessionLocal
from app.models.course_model import Course

def recomendar_curso(perfil):
    db = SessionLocal()
    try:
        cursos_db = db.query(Course).all()
        cursos = []
        for c in cursos_db:
            cursos.append({
                "id": c.id,
                "nome": c.nome,
                "descricao": c.descricao,
                "salario_medio": c.salario_medio,
                "skills": c.skills,
                "dificuldade": c.dificuldade,
                "duracao": c.duracao,
                "tags": c.tags
            })
    finally:
        db.close()
    
    matematica = perfil.matematica
    pratico = perfil.pratico
    tempo = perfil.tempo

    # Pontuação para cada curso
    scores = []
    for curso in cursos:
        score = 0
        tags = curso["tags"]
        
        # Lógica de pontuação
        if "matematica" in tags and matematica >= 7: score += 3
        if "teorico" in tags and matematica >= 6: score += 2
        if "pratico" in tags and pratico >= 7: score += 3
        if "rapido" in tags and tempo == "curto": score += 4
        if "longo" in tags and tempo == "longo": score += 2
        if "complexo" in tags and matematica >= 8: score += 2
        
        scores.append((score, curso))
    
    # Ordena pelo score e retorna o melhor
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[0][1] # Retorna o objeto do curso completo