from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn, os

app = FastAPI()

# Serve Dashboard from root directory
@app.get("/", response_class=HTMLResponse)
def dashboard():
    with open("dashboard.html", "r") as f:
        return f.read()

@app.get("/health")
def health():
    return {"status": "healthy", "system": "ai-nexus", "version": "1.0.0"}

@app.get("/status")
def status():
    return {
        "status": "operational",
        "three_tier_architecture": {
            "tier_1": "seekers - market scanning",
            "tier_2": "relayers - execution with flash loans & gasless", 
            "tier_3": "orchestrator - AI optimization"
        },
        "features": [
            "$100M Flash Loans",
            "Gasless Transactions", 
            "AI Optimization",
            "Three-Tier Architecture"
        ],
        "schedule": "24/7/365"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print("íº€ AI-Nexus Dashboard - All Endpoints Active")
    uvicorn.run(app, host="0.0.0.0", port=port)
