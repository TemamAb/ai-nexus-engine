"""
AI-NEXUS INSTITUTIONAL DASHBOARD - PRODUCTION GRADE
Maintaining ALL $100M flash loan capacity and institutional features
"""
from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

app = FastAPI(
    title="AI-Nexus Institutional Dashboard",
    description="$100M Flash Loan Arbitrage Engine - Production Grade",
    version="2.0.0"
)

# CRITICAL: Include ALL institutional APIs - NO COMPROMISES
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
    print("âœ… ALL INSTITUTIONAL APIS LOADED - NO COMPROMISES")
except Exception as e:
    print(f"íº¨ INSTITUTIONAL API ERROR: {e}")
    # This is critical - we cannot proceed without institutional features
    raise

@app.get("/")
async def root():
    return {
        "system": "AI-Nexus Industrial Platform",
        "status": "active",
        "capacity": "$100,000,000",
        "daily_target": "$250,000",
        "core_features": [
            "Three-Tier Architecture (8+6+3 Nodes)",
            "Gasless Mode (ERC-4337)",
            "AI Auto-Optimization 24/7/365",
            "5 Non-Custodial Wallet Support"
        ],
        "dashboard": "/api/institutional/dashboard"
    }

@app.get("/dashboard")
async def dashboard_redirect():
    return {
        "message": "AI-Nexus Institutional Dashboard",
        "access_url": "https://ai-nexus-engine.onrender.com/api/institutional/dashboard",
        "performance_guarantee": "FULL INSTITUTIONAL GRADE - NO COMPROMISES"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
