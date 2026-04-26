# TechPath AI

Um sistema inteligente que utiliza IA para recomendar cursos na área de tecnologia com base no perfil do usuário.

---

## Sobre o Projeto

O **TechPath AI** é uma aplicação fullstack simples que simula um orientador de carreira em tecnologia.

O usuário descreve seu perfil (ex: preferências, afinidade com matemática, objetivo de carreira), e o sistema:

1. Analisa essas informações
2. Aplica uma lógica de recomendação
3. Utiliza IA para gerar uma explicação personalizada
4. Retorna uma sugestão de curso ideal

---

## 🧠 Como Funciona

O sistema é dividido em duas partes principais:

### 🔹 Backend (Python + FastAPI)

Responsável por:
- Receber os dados do usuário
- Aplicar regras de recomendação
- Integrar com IA (Groq)
- Retornar resposta estruturada

Fluxo:

---

### 🔹 Frontend (HTML + CSS + JS)

Responsável por:
- Interface estilo chat
- Captura de input do usuário
- Exibição da resposta
- Animações e experiência do usuário

---

## ⚙️ Tecnologias Utilizadas

### Backend
- Python
- FastAPI
- Uvicorn
- Requests
- python-dotenv

### Frontend
- HTML5
- CSS3
- JavaScript
- GSAP (animações)

---

## 📁 Estrutura do Projeto
````
backend/
├── app/
│ ├── main.py
│ ├── routes/
│ ├── services/
│ ├── models/
│ └── core/
├── front/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── .env
└── requirements.txt
````

---

## 🔌 API

### Endpoint principal

### Exemplo de requisição:

```json
{
  "matematica": 3,
  "pratico": 8,
  "tempo": "curto"
}
```
### Exemplo de resposta:
```json
{
  "curso_recomendado": "Análise e Desenvolvimento de Sistemas (ADS)",
  "explicacao": "..."
}
```

# Lógica de Recomendação

A recomendação é baseada em regras simples:

- **Baixa afinidade com matemática →** ADS  
- **Alta afinidade com matemática →** Ciência da Computação  
- **Tempo curto →** cursos tecnólogos  
- **Caso intermediário →** Sistemas de Informação  

A IA entra para:

- Explicar a escolha  
- Tornar a resposta mais natural  
- Melhorar a experiência do usuário  

## 💬 Interface (Chat)

O frontend simula uma conversa:

- Usuário digita seu perfil  
- Sistema responde como um orientador  
- Histórico de mensagens é exibido  
- Interface inspirada em chat moderno  

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```
## ▶️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone <https://github.com/lazaaro01/TechPath-AI>
cd backend
```
## Criar ambiente virtual
```json
python -m venv venv
venv\Scripts\activate  # Windows
 ou
source venv/bin/activate  # Linux/Mac
```
## Instalr dependências

```json
pip install -r requirements.txt
```

## Rodar o backend
``` json
python -m uvicorn app.main:app --reload

A API estará disponível em:

http://localhost:8000
Swagger: http://localhost:8000/docs
```
## Rodar o frontend

Basta abrir o arquivo:

front/index.html

## Desenvolvido por 💻

Projeto pessoal de **Lázaro Vasconcelos**