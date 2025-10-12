export function play_template(content) {
  const { embed_url, title } = content;

  return `
    <div class="w-full rounded-xl overflow-hidden">
      <h1 class="text-xl sm:text-3xl text-slate-700 font-bold mb-2">${title}</h1>
      <iframe
        src="${embed_url}"
        class="w-full aspect-video rounded-xl overflow-hidden"
        allowfullscreen
      ></iframe>
    </div>
  `;
}
