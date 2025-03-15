from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request):
    raw_body = await request.body()
    print(f"🔍 RAW BODY: {raw_body}")  # <-- Debugging
    try:
        data = json.loads(raw_body.decode("utf-8"))
    except json.JSONDecodeError:
        data = None
    return {"status": "success", "received": data, "generatedCode": "console.log(Hello from CodeHook!);"}
