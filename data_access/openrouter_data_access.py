from infrastructure.openrouter_client import OpenRouterClient

class OpenRouterDataAccess:
    def __init__(self):
        self.client = OpenRouterClient()  # Asegurar que la API Key esté accesible

    def fetch_response(self, question: str):
        return self.client.get_response(question)
