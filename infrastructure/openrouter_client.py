import requests  # importamos requests por que sirve para hacer peticiones a una url
import json  # importamos json por que sirve para trabajar con archivos json
import random  # importamos random para generar la sopa de letras

class OpenRouterClient:  # aqui creamos la clase OpenRouterClient
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = "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"
    # aqui creamos las variables API_URL y API_KEY, API_URL es la url a la que haremos la peticion y API_KEY es la clave que nos permitira hacer la peticion

    def get_response(self, question: str):
        headers = {"Authorization": f"Bearer {self.API_KEY}"}
        print("API Key used:", self.API_KEY)  # <-- Verifica si la API Key es correcta
        print("Sending headers:", headers)  # <-- Verifica los headers
        response = requests.post(
            url=self.API_URL,
            headers=headers,
            data=json.dumps({
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": "user", "content": question}]
            })
        )
        print(response.status_code, response.text)  # <-- Verifica la respuesta completa
        return response.json()
