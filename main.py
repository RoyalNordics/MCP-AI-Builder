from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request):
    raw_body = await request.body()  # Læs rå body
    print("🔍 RAW BODY:", raw_body.decode())  # Debug print i logs

    try:
        data = await request.json()  # Prøv at parse JSON
        print("✅ PARSED JSON:", data)  # Debug print
        return {"status": "success", "received": data}
    except Exception as e:
        print("❌ ERROR:", str(e))  # Debug fejl
        return {"status": "error", "message": str(e), "raw_body": raw_body.decode()}
