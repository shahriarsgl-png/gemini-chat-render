const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const log = document.getElementById("chat-log");

function addMessage(text, cls) {
  const div = document.createElement("div");
  div.className = `message ${cls}`;
  div.textContent = text;
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";
  input.disabled = true;

  const thinkingEl = document.createElement("div");
  thinkingEl.className = "message bot";
  thinkingEl.textContent = "Thinking...";
  log.appendChild(thinkingEl);
  log.scrollTop = log.scrollHeight;

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await res.json();

    thinkingEl.remove();

    if (!res.ok) {
      addMessage(data.error || "Something went wrong.", "error");
    } else {
      addMessage(data.reply, "bot");
    }
  } catch (err) {
    thinkingEl.remove();
    addMessage("Network error. Please try again.", "error");
  } finally {
    input.disabled = false;
    input.focus();
  }
});
