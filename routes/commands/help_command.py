from .command_helper import newJson

def help_command(command, confidence):
    HELP_HTML = """
    <h2 class="text-xl font-semibold mb-2 text-slate-700">Available Commands</h2>
    <ul class="list-disc pl-6 text-slate-600 space-y-1">
      <li><strong>joke</strong> — Tells a random joke.</li>
      <li><strong>weather</strong> — Shows weather info for a city (e.g. "weather Manila").</li>
      <li><strong>quote</strong> — Displays an inspirational quote.</li>
      <li><strong>news</strong> — Fetches the latest news headlines.</li>
      <li><strong>play</strong> — Plays a song (e.g. "play Impacto by Ejambre").</li>
      <li><strong>search</strong> — Searches the web or knowledge base.</li>
      <li><strong>email</strong> — Sends or reads an email.</li>
      <li><strong>wiki</strong> — Looks up something on Wikipedia.</li>
      <li><strong>dictionary</strong> — Defines a word.</li>
      <li><strong>thesaurus</strong> — Finds synonyms for a word.</li>
      <li><strong>help</strong> — Shows this command list.</li>
    </ul>
    """.strip()

    return newJson(command, confidence, HELP_HTML)
