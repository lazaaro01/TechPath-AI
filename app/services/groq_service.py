import requests
from app.core.config import GROQ_API_KEY

def gerar_explicacao(curso, perfil):
    url = "https://api.groq.com/openai/v1/chat/completions"

    prompt = f"""
    Explique de forma simples e amigável por que o curso "{curso}" é ideal para uma pessoa com o seguinte perfil:

    - Afinidade com matemática: {perfil.matematica}/10
    - Preferência por prática: {perfil.pratico}/10
    - Tempo disponível: {perfil.tempo}

    Seja direto e motivador.
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    
    return "Não foi possível gerar explicação no momento."