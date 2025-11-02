from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def root():
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

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tiers")
def tiers():
    return {
        "tier_1": "seekers - active",
        "tier_2": "relayers - active", 
        "tier_3": "orchestrator - active"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
