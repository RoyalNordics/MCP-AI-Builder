from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/upload_recipe")
async def upload_recipe(file: UploadFile = File(...)):
    contents = await file.read()
    return {"message": "Recipe received!", "filename": file.filename}

