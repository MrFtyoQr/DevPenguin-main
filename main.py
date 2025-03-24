from fastapi import FastAPI
from api.routers1 import router
from api.routers1 import router as routers1_router
from api.pokemon_router import pokemon_router
from api.routers import pokemon
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

# Load environment variables
load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/api")
app.include_router(pokemon_router, prefix="/pokemon")
app.include_router(pokemon.router)
app.include_router(routers1_router, prefix="/api")  # Ya incluye el router con el prefijo /api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O especifica la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Punto de entrada para Heroku
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
