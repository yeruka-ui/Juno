import humanMsg from "./humanMsg.js";
import {botMsg, errorMsg, loadingMsg} from "./botMsg.js";
import {dictionary_template} from "./response_template/dictionary_template.js";
import {thesaurus_template} from "./response_template/thesaurus_template.js";
import {news_template} from "./response_template/news_template.js";

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

            // TODO :: REFACTOR TO SWITCH CASES

            if (String(data.command) === 'news') {
                const content = data.content
                parent.appendChild(botMsg(news_template(content)));
                console.log(JSON.stringify(data, null, 2));
            }
            else if (String(data.command) === 'dictionary') {
                const content = data.content

                parent.appendChild(botMsg(dictionary_template(content)));

                console.log(JSON.stringify(data, null, 2));
            }
            else if (String(data.command) === 'thesaurus') {
                const content = data.content

                parent.appendChild(botMsg(thesaurus_template(content)));

                console.log(JSON.stringify(data, null, 2));
            }

            //default msg formatting
            else {
                parent.appendChild(botMsg(data.content));
                console.log(JSON.stringify(data, null, 2));
            }

        } else {
            const msg = `Error: ${JSON.stringify(data, null, 2)}`;
            parent.appendChild(errorMsg(msg));
        }

    } catch (err) {
        parent.appendChild(errorMsg(`Network/Parse error: ${err.message}`));
    }
}

formListener();
