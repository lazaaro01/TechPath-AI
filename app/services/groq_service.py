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
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    
    return "Não foi possível gerar explicação no momento."

def extrair_perfil(texto_usuario):
    url = "https://api.groq.com/openai/v1/chat/completions"

    prompt = f"""
    Analise o texto do usuário e extraia três informações em formato JSON:
    1. matematica (int, 1-10): Afinidade com matemática/lógica.
    2. pratico (int, 1-10): Preferência por atividades práticas/mão na massa.
    3. tempo (str, "curto", "medio" ou "longo"): Disponibilidade de tempo.

    Texto: "{texto_usuario}"

    Responda APENAS o JSON. Exemplo: {{"matematica": 5, "pratico": 8, "tempo": "curto"}}
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "Você é um assistente que extrai dados estruturados de textos."},
            {"role": "user", "content": prompt}
        ],
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            import json
            return json.loads(response.json()["choices"][0]["message"]["content"])
    except Exception:
        pass
    
    return {"matematica": 5, "pratico": 5, "tempo": "medio"}

def gerar_roadmap(curso_nome, perfil):
    url = "https://api.groq.com/openai/v1/chat/completions"

    prompt = f"""
    Crie um roadmap de estudos simplificado de 6 meses para o curso "{curso_nome}".
    Leve em conta que o usuário tem:
    - Afinidade com matemática: {perfil.matematica}/10
    - Preferência por prática: {perfil.pratico}/10

    Formate a resposta em JSON com uma lista de objetos chamados "meses", onde cada objeto tem:
    - numero (int)
    - foco (str)
    - atividades (lista de strings)

    Responda APENAS o JSON. Exemplo: {{"meses": [{{"numero": 1, "foco": "Lógica", "atividades": ["Ver aulas", "Praticar"]}}]}}
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Você é um mentor de carreira experiente."},
            {"role": "user", "content": prompt}
        ],
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            import json
            content = response.json()["choices"][0]["message"]["content"]
            return json.loads(content)["meses"]
    except Exception as e:
        print(f"Erro no roadmap: {e}")
    
    return []