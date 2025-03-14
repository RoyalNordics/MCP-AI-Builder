from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI
import os
import requests

app = FastAPI()

# CORS Middleware (kun én gang)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API-konfiguration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY, temperature=0.5)

# Endpoints
@app.get("/")
def home():
    return {"message": "MCP Server Running"}

@app.get("/generate")
def generate_code(idea: str):
    response = llm.invoke(f"Generate Python FastAPI code for: {idea}")
    return {"generated_code": response}

# Endpoint til at uploade opskrifter
CODEHOOK_URL = "https://codehook.onrender.com/api/upload_recipe"

@app.post("/upload_recipe")
async def upload_recipe(file: UploadFile = File(...)):
    files = {
        "file": (file.filename, file.file, file.content_type)
    }
    response = requests.post(CODEHOOK_URL, files=files)
    return {"status": response.status_code, "message": response.text}
