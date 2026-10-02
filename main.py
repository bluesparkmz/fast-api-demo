from fastapi import FastAPI

app = FastAPI(title="Bluesparkcloud App")

@app.get("/")
def root():
    return {"message": "Hello from Bluesparkcloud"}

@app.get("/health")
def health():
    return {"status": "ok"}


