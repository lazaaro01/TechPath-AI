# TechPath AI

O **TechPath AI** é um mentor de carreira inteligente que utiliza Inteligência Artificial para analisar o perfil de usuários e recomendar o melhor caminho na área de tecnologia, fornecendo detalhes de mercado e um plano de estudos personalizado.

---

## Novas Funcionalidades (V2.0)

- **Análise de Linguagem Natural:** O sistema agora interpreta descrições complexas (ex: "Gosto de lógica mas prefere algo rápido") usando LLMs (Llama 3 via Groq).
- **Cards de Carreira Detalhados:** Recomendações completas com salário médio, habilidades (skills), duração e nível de dificuldade.
- **Roadmap de 6 Meses:** Geração automática de um plano de estudos mensal personalizado para o curso recomendado.
- **UI/UX Premium:** Interface moderna com modo escuro, efeitos de *glassmorphism* e animações fluidas via GSAP.
- **📚 Base de Conhecimento:** Sistema de recomendação baseado em uma base de dados estruturada (`courses.json`).

---

## 🧠 Como Funciona

1. **Entrada:** O usuário descreve seu perfil no chat de forma natural.
2. **Extração:** O Backend utiliza a Groq API para converter o texto em dados estruturados (Afinidade matemática, Prática e Tempo).
3. **Match:** O sistema busca na base de dados o curso que melhor se adapta às pontuações do usuário.
4. **Geração:** A IA gera uma explicação motivadora e um roadmap de estudos de 6 meses.
5. **Exibição:** O Frontend renderiza o card do curso e o plano de estudos com animações.

---

## ⚙️ Tecnologias Utilizadas

### Backend
- **Python / FastAPI:** Servidor de alta performance.
- **Groq Cloud (Llama 3):** IA de altíssima velocidade para processamento de texto.
- **Pydantic:** Validação de dados estruturados.

### Frontend
- **HTML5 / CSS3:** Estilização premium com variáveis e dark mode.
- **JavaScript (Vanilla):** Lógica de chat e integração com API.
- **GSAP:** Animações de interface.

---

## 📁 Estrutura do Projeto
```
├── app/
│   ├── data/
│   │   └── courses.json      # Base de dados de cursos
│   ├── models/
│   │   └── user_profile.py   # Modelos Pydantic
│   ├── routes/
│   │   └── recommend.py      # Endpoints da API
│   ├── services/
│   │   ├── groq_service.py   # Integração com IA
│   │   └── recommendation_service.py # Lógica de match
│   ├── main.py               # Arquivo principal
│   └── core/
│       └── config.py         # Configurações de env
├── front/
│   ├── index.html            # Interface
│   ├── style.css             # Estilos Premium
│   └── script.js             # Lógica do chat
├── .env                      # Chaves de API
└── requirements.txt          # Dependências
```

---

## 🔌 API

### `POST /recomendar_texto`
Endpoint que recebe a mensagem natural do usuário.

**Exemplo de requisição:**
```json
{
  "message": "Não gosto de muita matemática, quero algo bem prático e rápido para o mercado."
}
```

---

## ▶️ Como Executar o Projeto

1. **Configurar o Ambiente:**
   ```bash
   python -m venv venv
   source venv/bin/activate # ou venv\Scripts\activate no Windows
   pip install -r requirements.txt
   ```

2. **Configurar a API Key:**
   Crie um arquivo `.env` e adicione sua chave:
   ```env
   GROQ_API_KEY=gsk_your_key_here
   ```

3. **Rodar o Backend:**
   ```bash
   python -m uvicorn app.main:app --reload
   ```

4. **Rodar o Frontend:**
   Abra o arquivo `front/index.html` em qualquer navegador moderno.

---

## Desenvolvido por 💻

Projeto pessoal de **Lázaro Vasconcelos**