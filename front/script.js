const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send-btn");

function addMessage(text, type, isHtml = false) {
  const msg = document.createElement("div");
  msg.classList.add("message", type);
  
  if (isHtml) {
    msg.innerHTML = text;
  } else {
    msg.innerText = text;
  }

  chat.appendChild(msg);

  gsap.from(msg, {
    opacity: 0,
    y: 20,
    scale: 0.9,
    duration: 0.5,
    ease: "back.out(1.7)"
  });

  chat.scrollTop = chat.scrollHeight;
  return msg;
}

function showTyping() {
  const typing = document.createElement("div");
  typing.classList.add("message", "bot", "typing");
  typing.innerHTML = `<span></span><span></span><span></span> Analisando perfil e gerando rota...`;
  chat.appendChild(typing);
  chat.scrollTop = chat.scrollHeight;
  return typing;
}

async function enviar() {
  const texto = input.value.trim();

  if (!texto) return;

  input.value = "";
  input.disabled = true;
  sendBtn.disabled = true;

  addMessage(texto, "user");

  const typingIndicator = showTyping();

  try {
    const response = await fetch("http://localhost:8000/recomendar_texto", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: texto })
    });

    if (!response.ok) throw new Error("Falha na API");

    const data = await response.json();
    chat.removeChild(typingIndicator);

    const curso = data.curso_recomendado;
    
    let skillsHtml = curso.skills.map(s => `<span class="skill-tag">${s}</span>`).join("");
    
    let roadmapHtml = data.roadmap.map(m => `
      <div class="roadmap-step">
        <h5>Mês ${m.numero}: ${m.foco}</h5>
        <ul>${m.atividades.map(a => `<li>• ${a}</li>`).join("")}</ul>
      </div>
    `).join("");

    const botMsg = `
      <strong>✨ Recomendação Encontrada:</strong>
      
      <div class="course-card">
        <h4>${curso.nome}</h4>
        <p style="font-size: 0.85rem; color: var(--text-muted);">${curso.descricao}</p>
        
        <div class="course-info-grid">
          <div class="info-item">
            <label>Salário Médio</label>
            <span>${curso.salario_medio}</span>
          </div>
          <div class="info-item">
            <label>Duração</label>
            <span>${curso.duracao}</span>
          </div>
          <div class="info-item">
            <label>Dificuldade</label>
            <span>${curso.dificuldade}</span>
          </div>
        </div>

        <div class="skills-tags">${skillsHtml}</div>
      </div>

      <p style="margin-top: 10px;">${data.explicacao}</p>

      <div class="roadmap-container">
        <h4 style="font-size: 0.95rem; margin-bottom: 15px; color: var(--primary-glow);">🚀 Seu Roadmap de 6 Meses</h4>
        ${roadmapHtml}
      </div>
    `;

    addMessage(botMsg, "bot", true);

  } catch (err) {
    console.error(err);
    if (typingIndicator.parentNode) chat.removeChild(typingIndicator);
    addMessage("Ops! Tive um problema ao processar sua rota. Tente novamente.", "bot");
  } finally {
    input.disabled = false;
    sendBtn.disabled = false;
    input.focus();
  }
}

input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") enviar();
});

window.onload = () => {
  setTimeout(() => {
    addMessage("👋 Olá! Vamos encontrar seu caminho na tecnologia e criar um plano de estudos para você?", "bot");
  }, 500);
};

function abrirModal() {
  document.getElementById("modal").classList.remove("d-none");
  gsap.from(".modal-content", { scale: 0.8, opacity: 0, duration: 0.3 });
}

function fecharModal() {
  gsap.to(".modal-content", {
    scale: 0.8, opacity: 0, duration: 0.2,
    onComplete: () => document.getElementById("modal").classList.add("d-none")
  });
}