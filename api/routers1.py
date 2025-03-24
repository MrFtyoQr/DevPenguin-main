# api/routers.py
from fastapi import APIRouter, HTTPException#Importamos APIRouter y HTTPException de fastapi
from services.openrouter_service import OpenRouterService#Importamos la clase OpenRouterService de services.openrouter_service
from services.word_search_service import WordSearchService  # Importamos el nuevo servicio
from services.code_generation_service import CodeGenerationService  # Importamos el nuevo servicio

router = APIRouter()#aqui creamos el router
service = OpenRouterService()#aqui inicializamos la clase OpenRouterService

@router.post("/ask")#aqui creamos la ruta /ask que recibe un metodo post
def ask_question(question: str):#aqui creamos el metodo ask_question que recibe un parametro question que es un string
    try:
        response = service.get_response(question)#aqui creamos la variable response que es el metodo get_response que se encuentra en la clase OpenRouterService que recibe un parametro question que es un string
        return {"response": response}#aqui retornamos un diccionario con la clave response y el valor response
    except Exception as e:#aqui manejamos la excepcion
        raise HTTPException(status_code=500, detail=str(e))#aqui lanzamos una excepcion HTTPException con el status_code 500 y el detalle de la excepcion

@router.post("/word-search")  # Nueva ruta para generar sopa de letras
def generate_word_search(topic: str, size: int = 10):
    try:
        word_search = WordSearchService.generate_word_search(topic, size)
        return {"word_search": word_search}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-code")  # Nueva ruta para generar código
def generate_code(prompt: str, language: str = "Python", explanation: bool = True):
    """
    Genera un código sencillo basado en el prompt proporcionado.
    :param prompt: Instrucción para generar el código.
    :param language: Lenguaje de programación deseado.
    :param explanation: Indica si se necesita una explicación del código.
    :return: Código generado.
    """
    try:
        code = CodeGenerationService.generate_code(prompt, language, explanation)
        if not code:
            raise ValueError("No se pudo generar el código.")
        return {"code": code}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor.")