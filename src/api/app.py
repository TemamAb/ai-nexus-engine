from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import institutional APIs
from .institutional_api import router as institutional_router
from .wallet_api import router as wallet_router
from .live_metrics import router as metrics_router
from .execution_monitor import router as execution_router
from .risk_dashboard import router as risk_router
from .profit_api import router as profit_router

app = FastAPI(title="AI-Nexus Institutional API", version="1.0.0")

# CORS for institutional dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all institutional endpoints
app.include_router(institutional_router, prefix="/api/institutional", tags=["institutional"])
app.include_router(wallet_router, prefix="/api/wallet", tags=["wallet"])
app.include_router(metrics_router, prefix="/api/metrics", tags=["metrics"])
app.include_router(execution_router, prefix="/api/execution", tags=["execution"])
app.include_router(risk_router, prefix="/api/risk", tags=["risk"])
app.include_router(profit_router, prefix="/api/profit", tags=["profit"])

@app.get("/")
async def root():
    return {
        "status": "OPERATIONAL",
        "service": "AI-Nexus Institutional Backend",
        "version": "1.0.0",
        "capacity": "$1$1$1$1$1$1$1$1$100M Flash Loans",
        "profit_target": "$250,000 Daily"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "ai-nexus-institutional"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
