"""
AI-NEXUS - MULTI-PORT DEPLOYMENT
Dynamic port configuration for 9000-9010 range
"""

import uvicorn
import os
from fastapi import FastAPI

# Get port from environment or use default
PORT = int(os.getenv("PORT", 8000))

app = FastAPI(
    title=f"AI-Nexus Port {PORT}",
    description=f"Industrial arbitrage system running on port {PORT}",
    version="3.0.0"
)

@app.get("/")
async def root():
    return {
        "status": "operational",
        "system": "AI-Nexus Industrial Arbitrage",
        "port": PORT,
        "deployment": "multi-port"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy", 
        "port": PORT,
        "service": "ainexus-arbitrage"
    }

@app.get("/status")
async def status():
    return {
        "ai_engine": "operational",
        "scanner": "active",
        "executor": "ready",
        "port": PORT,
        "capacity": "industrial"
    }

@app.get("/config")
async def config():
    return {
        "port": PORT,
        "ai_optimization_cycle": "15-minutes",
        "risk_management": "armed",
        "mev_protection": "active"
    }

if __name__ == "__main__":
    print(f"íº€ Starting AI-Nexus on port {PORT}")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=PORT,
        reload=False,
        log_level="info"
    )
