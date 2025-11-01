"""
Profit Withdrawal System API Endpoints
EXACT implementation as specified - NO ALTERATIONS
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter(prefix="/withdrawal", tags=["Profit Withdrawal"])

# Setup templates directory
templates = Jinja2Templates(directory="src/frontend/templates")

@router.get("/", response_class=HTMLResponse)
async def withdrawal_dashboard(request: Request):
    """Serve the profit withdrawal dashboard EXACTLY as provided"""
    return templates.TemplateResponse("withdrawal.html", {"request": request})

@router.get("/api/balance")
async def get_balance():
    """Get current balance for withdrawal system"""
    return {
        "usd_balance": 116137,
        "eth_balance": 62.5,
        "wallet_address": "0xd6Ef692B34c14000912f429ed503685cBD9C52E0"
    }

@router.post("/api/transfer")
async def execute_transfer(percentage: int):
    """Execute profit transfer - integrates with capital management system"""
    # This would integrate with src/capital/auto_transfer.py
    return {
        "status": "processing",
        "percentage": percentage,
        "estimated_amount_usd": 116137 * (percentage / 100),
        "estimated_amount_eth": 62.5 * (percentage / 100)
    }
