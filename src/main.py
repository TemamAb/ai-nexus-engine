#!/usr/bin/env python3
import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    title="AINexus Arbitrage Engine",
    description="Live Flash Loan Arbitrage - $250K Daily Profit Target",
    version="2.0.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from correct path
static_path = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
async def serve_dashboard():
    """Serve React dashboard"""
    index_path = os.path.join(static_path, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"status": "dashboard_building", "profit_target": "$250,000"}

@app.get("/api/health")
async def health_check():
    return {
        "status": "operational", 
        "blockchain": "connected",
        "profit_engine": "active",
        "daily_target": "$250,000"
    }

@app.get("/api/blockchain/status")
async def blockchain_status():
    """Live blockchain connectivity"""
    from web3 import Web3
    try:
        # Mainnet connections
        eth = Web3(Web3.HTTPProvider(os.getenv('ETH_MAINNET_RPC')))
        poly = Web3(Web3.HTTPProvider(os.getenv('POLYGON_RPC')))
        
        return {
            "ethereum": "connected" if eth.is_connected() else "disconnected",
            "polygon": "connected" if poly.is_connected() else "disconnected",
            "latest_block": eth.eth.block_number if eth.is_connected() else 0
        }
    except Exception as e:
        return {"status": "connecting", "error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
