import humanMsg from "./humanMsg.js"
import {botMsg, errorMsg} from "./botMsg.js";


function formListener() {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("userInput");
    const chatContainer = document.getElementById("chatContainer");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const message = input.value.trim()
        input.value = "";
        if(!message) return;

        //add message to chat container
        chatContainer.appendChild(humanMsg(message));

        await sendMessage(message, chatContainer);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    })
}

async function sendMessage(message, parent) {
     const res = await fetch("/api/ask", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message }),
        });
     const data = await res.json();

     if(data.reply) {
         parent.appendChild(botMsg(data.reply));
     }
     else {
         const msg = `Error: ${JSON.stringify(data)}`
         parent.appendChild(errorMsg(data));
     }
}

formListener()