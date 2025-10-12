export function dictionary_template(content) {
    // destructure content
    const word = content[0];
    const definition = content[2];

    // template
    const template = `
    <h1 class="text-xl sm:text-2xl font-bold mb-3">Definition of "${word}"</h1>
    <hr class="border-slate-600 border-1" />
    <p class="text-md sm:text-xl">${definition}</p>`;

    return template;
}
