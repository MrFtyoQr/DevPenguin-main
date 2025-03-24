import requests  # importamos requests por que sirve para hacer peticiones a una url
import json  # importamos json por que sirve para trabajar con archivos json
import os

class OpenRouterClient:
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    # Si la API key no está en variables de entorno, usa la hardcodeada (temporalmente)

    def get_response(self, question: str):
        headers = {"Authorization": f"Bearer {self.API_KEY}"}
        response = requests.post(
            url=self.API_URL,
            headers=headers,
            json={
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": "user", "content": question}]
            }
        )
        return response.json()
