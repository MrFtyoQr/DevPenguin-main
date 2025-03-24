# data_access/openrouter_data_access.py
import requests
from infrastructure.openrouter_client import OpenRouterClient#aqui importamos la clase OpenRouterClient

class OpenRouterDataAccess:#aqui creamos la clase OpenRouterDataAccess
    def __init__(self):#aqui inicializamos la clase
        self.client = OpenRouterClient()#aqui inicializamos la clase OpenRouterClient
    
    def fetch_response(self, question: str):
        headers = {"Authorization": f"Bearer {self.API_KEY}"}
        print("API Key en fetch_response:", self.API_KEY)
        response = requests.post(
            url=self.API_URL,
            headers=headers,
            json={"model": "google/gemini-2.0-flash-001", "messages": [{"role": "user", "content": question}]}
        )
        print("Código de respuesta:", response.status_code, "Respuesta:", response.text)
        return response.json()
