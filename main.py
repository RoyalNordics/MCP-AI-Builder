from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        raw_body = await request.body()
        if not raw_body:
            return {"status": "error", "message": "Empty request body received"}
        print(f"🔍 RAW BODY: {raw_body}")  # Skal vise data i logs
        return {"status": "success", "received": raw_body.decode("utf-8")}
    except Exception as e:
        return {"status": "error", "message": str(e)}
