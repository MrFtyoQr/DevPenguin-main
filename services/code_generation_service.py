from infrastructure.openrouter_client import OpenRouterClient

class CodeGenerationService:
    @staticmethod
    def generate_code(prompt: str, language: str, explanation: bool):
        """
        Genera un código sencillo basado en el prompt proporcionado.
        :param prompt: Instrucción para generar el código.
        :param language: Lenguaje de programación deseado.
        :param explanation: Indica si se necesita una explicación del código.
        :return: Código generado.
        """
        client = OpenRouterClient()
        full_prompt = f"Escribe un código en {language} que haga lo siguiente: {prompt}."
        if not explanation:
            full_prompt += " Solo proporciona el código sin ningún tipo de comentario o explicación."
        response = client.get_response(full_prompt)
        return response.get("choices", [{}])[0].get("message", {}).get("content", "No se pudo generar el código.")
