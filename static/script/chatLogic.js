import humanMsg from "./humanMsg.js";
import {botMsg, errorMsg} from "./botMsg.js";

function formListener() {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("userInput");
    const chatContainer = document.getElementById("chatContainer");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const message = input.value.trim();
        input.value = "";
        if (!message) return;

        // Add user message
        chatContainer.appendChild(humanMsg(message));

        await sendMessage(message, chatContainer);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    });
}

async function sendMessage(message, parent) {
    try {
        const res = await fetch("/api/ask", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message}),
        });

        if (!res.ok) {
            // handle 4xx/5xx responses
            const errText = await res.text();
            parent.appendChild(errorMsg(`Server Error ${res.status}: ${errText}`));
            return;
        }

        const data = await res.json();

        if (data.reply) {
            parent.appendChild(botMsg(data.reply));
            console.log(JSON.stringify(data));
        } else if (data.isCommand) {
            parent.appendChild(botMsg(data.content));
            console.log(JSON.stringify(data));
        } else {
            const msg = `Error: ${JSON.stringify(data, null, 2)}`;
            parent.appendChild(errorMsg(msg)); // ✅ pass string, not object
        }
    } catch (err) {
        parent.appendChild(errorMsg(`Network/Parse error: ${err.message}`));
    }
}

formListener();
