from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "project": "Master Agent",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
