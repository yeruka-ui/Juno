export function thesaurus_template(content) {
    //data
    const orig_word = content['orig_word']
    const synonyms = content['synonyms']?.join(', ') || 'None';
    const antonyms = content['antonyms']?.join(', ') || 'None';

    //template
    const template = `<h1 class="text-2xl font-bold mb-3">Thesaurus: "${orig_word}"</h1>
          <hr class="border-slate-600 border-1" />
          <h1 class="text-2xl font-bold">Synonyms:</h1>
          <p>${synonyms}</p>
          <br />
          <h1 class="text-2xl font-bold">Antonyms:</h1>
          <p>${antonyms}</p>
        </div>`
    return template
}