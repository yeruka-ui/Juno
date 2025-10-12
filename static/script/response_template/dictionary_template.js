export function dictionary_template(content) {
    //get content
    const word = content[0]
    const parts = content[1]
    const definition = content[2]

    //template
    const template = `
    <h1 class="text-2xl font-bold mb-3">Definition of ${word}</h1>
    <hr class="border-slate-600 border-1" />
    <h1 class="text-xl mb-3">Parts of Speech: ${parts}</h1>
    <p> ${definition} </p>`;

    return template
}