from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "operational", 
        "port": 8001,
        "system": "AI-Nexus Three-Tier",
        "features": ["$100M Flash Loans", "Gasless", "AI Optimization", "Three-Tier"],
        "schedule": "24/7/365"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    print("AI-NEXUS RUNNING ON PORT 8001")
    uvicorn.run(app, host="0.0.0.0", port=8001, access_log=False)
