import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "nvidia/nemotron-nano-9b-v2:free",
    "messages": [
      {
        "role": "Juno",
        "content": "What is the meaning of life?"
      }
    ],
    
  })
)