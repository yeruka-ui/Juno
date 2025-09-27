//bot message div
export function botMsg(msg) {
    const message = document.createElement('div')
    message.className = "h-fit w-[85%] sm:w-[700px] bg-gradient-to-r from-emerald-100 to-teal-100 rounded-2xl self-start drop-shadow text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-slate-600"
    message.innerHTML = msg;

    return message;
}
//bot message error
export function errorMsg(error) {
    const message = document.createElement('div')
    message.className = "h-fit w-[85%] sm:w-[700px] bg-red-100 rounded-2xl self-start drop-shadow text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-red-600"
    message.innerHTML = error;

    return message;
}

