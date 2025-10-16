export default function wiki_template(content) {

    if (content['error']) {
        return "Unable to find your query"
    }

  const title = content["title"];
  const body = content["body"];
  const url = content["url"];
  const thumbnail =
    content["thumbnail"] ?? "https://placehold.co/600x400?text=No+Image";

  const template = `
  <a 
    href="${url}" 
    target="_blank"
    class="flex flex-col sm:flex-row items-start gap-4 rounded-xl hover:brightness-95 transition"
  >
    <img
      src="${thumbnail}"
      alt="${title}"
      class="w-fit h-fit sm:w-48 sm:h-48 object-cover rounded-xl flex-shrink-0"
    />
    <div class="flex flex-col justify-between bg-transparent text-left">
      <h1 class="text-slate-700 text-2xl font-bold mb-2">${title}</h1>
       <hr class="my-3 border-slate-700 border" />
      <p class="text-slate-700 text-[18px] leading-relaxed">${body}</p>
    </div>
  </a>

  `;

  return template;
}
