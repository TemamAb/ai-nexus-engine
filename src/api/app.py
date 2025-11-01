"""
AINEXUS FastAPI Routes - Clean encoding
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="AINEXUS Arbitrage Engine",
    description="Industrial-Scale AI-Driven Flash Loan Arbitrage System",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class SimulationRequest(BaseModel):
    duration: int = 3600
    capital: float = 1000.0

class LiveExecuteRequest(BaseModel):
    strategy_id: str
    amount: float

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AINEXUS v2.0 - Hyper-Orchestrator</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #0f0f23; color: #00ff00; }
            .container { max-width: 1200px; margin: 0 auto; }
            .header { text-align: center; margin-bottom: 40px; border-bottom: 1px solid #00ff00; padding-bottom: 20px; }
            .status { background: #1a1a2e; padding: 20px; border-radius: 10px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>AINEXUS v2.0 - HYPER-ORCHESTRATOR</h1>
                <p>Industrial-Scale Arbitrage Flash Loan Engine - DEPLOYED SUCCESSFULLY</p>
            </div>
            <div class="status">
                <h3>System Status: ACTIVE</h3>
                <p><strong>Deployment Time:</strong> 2024-01-15 10:30:00 UTC</p>
                <p><strong>Version:</strong> 2.0.0 Hyper-Orchestrator</p>
                <p><a href="/docs" style="color: #00ff00;">View API Documentation</a></p>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ainexus",
        "version": "2.0.0",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/metrics")
async def get_metrics():
    return {
        "system": {
            "status": "operational",
            "deployment": "render",
            "ai_engine": "ready"
        },
        "timestamp": datetime.now().isoformat()
    }

# Import and include industrial API if available
try:
    from api.industrial_api import router as industrial_router
    app.include_router(industrial_router)
    print("Industrial API endpoints loaded")
except ImportError as e:
    print(f"Industrial API not available: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Import and include withdrawal system
from api.withdrawal import router as withdrawal_router
app.include_router(withdrawal_router)

# Import and include transfer mode API
from api.transfer_api import router as transfer_api_router
app.include_router(transfer_api_router)
