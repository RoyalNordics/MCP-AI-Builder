from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        raw_body = await request.body()
        if not raw_body.strip():
            return {"status": "error", "message": "Empty request body received"}
        
        received_data = raw_body.decode("utf-8")
        print(f"🔍 RAW BODY: {received_data}")  # Logger request body

        return {"status": "success", "received": received_data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
