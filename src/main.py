from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI-Nexus Live", "build": "rust-free"}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
