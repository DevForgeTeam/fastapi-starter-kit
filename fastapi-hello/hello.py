from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "service": "fastapi-hello"}

@app.get("/health")
def health():
    return {"status" "healthy"}
