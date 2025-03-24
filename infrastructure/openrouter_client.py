import requests  # importamos requests por que sirve para hacer peticiones a una url
import json  # importamos json por que sirve para trabajar con archivos json
import random  # importamos random para generar la sopa de letras

class OpenRouterClient:  # aqui creamos la clase OpenRouterClient
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = "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"
    # aqui creamos las variables API_URL y API_KEY, API_URL es la url a la que haremos la peticion y API_KEY es la clave que nos permitira hacer la peticion

    def get_response(self, question: str):  # aqui creamos el metodo get_response que recibe un parametro question
        headers = {"Authorization": f"Bearer {self.API_KEY}"}  # aqui creamos la variable headers
        print("Sending headers:", headers)  # Verifica los encabezados
        response = requests.post(
            url=self.API_URL,
            headers=headers,
            data=json.dumps({
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": "user", "content": question}]
            })
        )  # aqui creamos la variable response que es la respuesta de la peticion post
        print(response.status_code)  # Verifica el código de estado
        return response.json()