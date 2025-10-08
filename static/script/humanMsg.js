export default function humanMsg(msg) {
    const message = document.createElement('div')
    message.className = "h-fit w-fit bg-white rounded-2xl self-end drop-shadow font-[Inter] text-[20px] text-start sm:text-2xl p-2 sm:p-6 text-wrap text-slate-600"
    message.innerHTML = msg;

    return message;
}