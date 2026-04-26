import json
import os

def carregar_cursos():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "courses.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def recomendar_curso(perfil):
    cursos = carregar_cursos()
    
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