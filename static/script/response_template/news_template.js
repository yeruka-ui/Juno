export function news_template(content) {
  let html = `
    <div class="flex flex-col items-start justify-center gap-8 sm:gap-12">
      <h1 class="text-center sm:text-start text-3xl text-slate-700 font-bold mb-2">
        Latest Headlines
      </h1>
  `;

    content.forEach((news) => {
        const title = news['title'];
        const body = (news['content'] || '');
        const imageUrl = news['imageUrl'];
        const url = news['url'];

        html += `
    <div class="flex flex-col sm:flex-row items-start justify-center gap-2 sm:gap-4 w-full h-fit">
       <a href="${url}" target="_blank">
            <img src="${imageUrl}" alt="${title}" class="h-fit w-fit sm:max-w-[400px] object-contain rounded-xl" />
      </a>
        <div>
             <h1 class="text-slate-700 text-md sm:text-2xl font-bold">${title}</h1>
             <p class="text-slate-700 text-md sm:text-xl">${body}</p>
        </div>
    </div>
    `;
    });
    html += '</div>';
    return html;
}
