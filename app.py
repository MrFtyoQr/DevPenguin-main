from fastapi import FastAPI
from api.routers1 import router
from api.routers1 import router as routers1_router
from api.pokemon_router import pokemon_router
from api.routers import pokemon
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/api")
app.include_router(pokemon_router, prefix="/pokemon")
app.include_router(pokemon.router)
app.include_router(routers1_router, prefix="/api")  # Ya incluye el router con el prefijo /api