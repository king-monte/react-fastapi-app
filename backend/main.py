from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/data")
def data():
    return {
        "message": "Hello from FastAPI backend"
    }

