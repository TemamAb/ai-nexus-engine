from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

app = FastAPI(title="AI-Nexus Institutional Dashboard")

# Include all institutional APIs
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
    print("✅ All institutional APIs loaded")
except Exception as e:
    print(f"⚠️ API loading warning: {e}")

@app.get("/")
async def root():
    return {"message": "AI-Nexus Institutional Dashboard"}

@app.get("/dashboard")
async def dashboard():
    return {
        "dashboard": "Institutional Dashboard",
        "access_url": "https://ai-nexus-engine.onrender.com/api/institutional/dashboard",
        "endpoints": {
            "metrics": "/api/metrics/live",
            "execution": "/api/execution/active-trades",
            "risk": "/api/risk/metrics", 
            "wallets": "/api/wallet/supported-wallets",
            "performance": "/api/institutional/performance"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
