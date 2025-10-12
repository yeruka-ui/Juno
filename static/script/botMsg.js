import { chatAnimation } from "./animationHandler.js";

export function botMsg(msg) {
    const message = document.createElement('div');
    message.className = "chat h-fit w-fit max-w-[90%] sm:max-w-[95%] bg-gradient-to-r sm:p-6 p-4 from-emerald-100 to-teal-100 rounded-2xl self-start drop-shadow text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-slate-600";
    message.innerHTML = msg;
    chatAnimation(message);
    return message;
}

export function errorMsg(error) {
    const message = document.createElement('div');
    message.className = "chat h-fit w-fit max-w-[90%] sm:max-w-[95%] bg-red-100 sm:p-6 p-4 rounded-2xl self-start drop-shadow text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-red-600";
    message.innerHTML = error;
    chatAnimation(message);
    return message;
}

export function loadingMsg() {
    const message = document.createElement('div');
    message.className = "chat loader-body h-fit w-fit max-w-[90%] sm:max-w-[95%] sm:p-6 p-4 bg-gradient-to-r from-emerald-100 to-teal-100 rounded-2xl self-start drop-shadow text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-slate-600";
    const loader = document.createElement('div');
    loader.className = 'loader'
    message.appendChild(loader);
    return message
}
