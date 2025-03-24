from fastapi import FastAPI
from api.routers1 import router as routers1_router
from api.pokemon_router import pokemon_router
from api.routers import pokemon
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

# Cargar variables de entorno
load_dotenv()

# Crear la app
app = FastAPI()

# Incluir routers
app.include_router(routers1_router, prefix="/api")
app.include_router(pokemon_router, prefix="/pokemon")
app.include_router(pokemon.router)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza con tu frontend si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Punto de entrada para desarrollo local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

