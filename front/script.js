const chat = document.getElementById("chat");

function addMessage(text, type) {
  const msg = document.createElement("div");
  msg.classList.add("message", type);
  msg.innerText = text;

  chat.appendChild(msg);

  gsap.from(msg, {
    opacity: 0,
    y: 10,
    duration: 0.4
  });

  chat.scrollTop = chat.scrollHeight;
}

async function enviar() {
  const input = document.getElementById("input");
  const texto = input.value;

  if (!texto) return;

  addMessage(texto, "user");
  input.value = "";

  addMessage("Analisando seu perfil...", "bot");

  try {
    const response = await fetch("http://localhost:8000/recomendar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        matematica: extrairNumero(texto, "matematica") || 5,
        pratico: extrairNumero(texto, "pratico") || 5,
        tempo: extrairTempo(texto)
      })
    });

    const data = await response.json();

    chat.removeChild(chat.lastChild);

    addMessage(
      `💡 Curso recomendado: ${data.curso_recomendado}\n\n${data.explicacao}`,
      "bot"
    );

  } catch (err) {
    addMessage("Erro ao conectar com o servidor.", "bot");
  }
}

function extrairNumero(texto, tipo) {
  if (texto.includes("não gosto de matemática")) return 2;
  if (texto.includes("gosto de matemática")) return 8;
  if (texto.includes("muito prático")) return 9;
  return null;
}

function extrairTempo(texto) {
  if (texto.includes("rápido")) return "curto";
  if (texto.includes("demorar")) return "longo";
  return "medio";
}
window.onload = () => {
  addMessage(
`👋 Olá! Eu sou seu orientador de carreira em tecnologia.

💡 Como funciona:
- Você descreve seu perfil (ex: "não gosto de matemática, quero algo prático")
- Eu analiso suas preferências
- E te recomendo um curso ideal + explicação personalizada

🚀 Pode começar escrevendo como você gosta de aprender!`,
  "bot"
  );
};
function abrirModal() {
    const btn = document.querySelector(".info-btn");

    btn.style.animation = "none";

  document.getElementById("modal").classList.remove("d-none");
}

function fecharModal() {
  document.getElementById("modal").classList.add("d-none");
}