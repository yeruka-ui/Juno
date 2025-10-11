import humanMsg from "./humanMsg.js";
import {botMsg, errorMsg, loadingMsg} from "./botMsg.js";


function formListener() {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("userInput");
    const chatContainer = document.getElementById("chatContainer");
    let isRunning = false;

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const message = input.value.trim();
        if (!message || isRunning) return;

        input.value = "";
        chatContainer.appendChild(humanMsg(message));
        chatContainer.scrollTop = chatContainer.scrollHeight;

        try {
            isRunning = true;
            chatContainer.appendChild(loadingMsg());
            await sendMessage(message, chatContainer);
        } finally {
            isRunning = false;
            const loader = document.querySelector('.loader-body');
            loader.remove();
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
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
            // no command
            parent.appendChild(botMsg(data.reply));
            console.log(JSON.stringify(data, null, 2));

            // with command
        } else if (data.isCommand) {
            parent.appendChild(botMsg(data.content));
            console.log(JSON.stringify(data, null, 2));

        } else {
            const msg = `Error: ${JSON.stringify(data, null, 2)}`;
            parent.appendChild(errorMsg(msg));
        }

    } catch (err) {
        parent.appendChild(errorMsg(`Network/Parse error: ${err.message}`));
    }
}

formListener();
