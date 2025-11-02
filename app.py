"""
AI-NEXUS INSTITUTIONAL DASHBOARD - Main Entry Point
This file is served by Render at: https://ai-nexus-engine.onrender.com
"""
from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

app = FastAPI(
    title="AI-Nexus Institutional Dashboard",
    description="Enterprise Flash Loan Arbitrage Engine",
    version="2.0.0"
)

# Include institutional APIs
try:
    from src.api.institutional_api import router as institutional_router
    from src.api.wallet_api import router as wallet_router
    from src.api.live_metrics import router as live_metrics_router
    from src.api.execution_monitor import router as execution_monitor_router
    from src.api.risk_dashboard import router as risk_dashboard_router
    
    app.include_router(institutional_router)
    app.include_router(wallet_router)
    app.include_router(live_metrics_router)
    app.include_router(execution_monitor_router)
    app.include_router(risk_dashboard_router)
    print("✅ Institutional APIs loaded")
except Exception as e:
    print(f"⚠️ API loading: {e}")

@app.get("/")
async def root():
    return {
        "service": "AI-Nexus Institutional Dashboard",
        "status": "active",
        "dashboard": "/api/institutional/dashboard",
        "docs": "/docs"
    }

@app.get("/dashboard")
async def dashboard():
    return {
        "message": "AI-Nexus Institutional Dashboard",
        "access_points": {
            "main_dashboard": "/api/institutional/dashboard",
            "live_metrics": "/api/metrics/live",
            "execution_monitor": "/api/execution/active-trades",
            "risk_dashboard": "/api/risk/metrics",
            "wallet_connect": "/api/wallet/supported-wallets"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
