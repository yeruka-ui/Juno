import { chatAnimation } from "./animationHandler.js";

export function botMsg(msg) {
    const message = document.createElement('div');
    message.className = "chat h-fit w-fit bg-gradient-to-r from-emerald-100 to-teal-100 rounded-2xl self-start drop-shadow text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-slate-600";
    message.innerHTML = msg;
    chatAnimation(message);
    return message;
}

export function errorMsg(error) {
    const message = document.createElement('div');
    message.className = "chat h-fit w-fit bg-red-100 rounded-2xl self-start drop-shadow text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-red-600";
    message.innerHTML = error;
    chatAnimation(message);
    return message;
}
