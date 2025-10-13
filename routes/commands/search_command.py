from .command_helper import newJson
from serpapi import GoogleSearch
import os

def get_search(command, confidence, query):
    if not confidence:
        confidence = 0.95  # default
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv('SERP_API')
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get('organic_results', [])
    if organic_results:
        snippet = organic_results[0].get('snippet', 'No snippet found.')
    else:
        snippet = "No search results found."

    return newJson(command, confidence, snippet)
