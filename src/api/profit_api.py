# coding: utf-8
"""
PURE BACKEND Profit Withdrawal API
NO FRONTEND - JSON API ONLY
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.capital.profit_withdrawal import withdrawal_engine, TransferMode

router = APIRouter(prefix="/api/profit", tags=["Profit Withdrawal"])

class WalletSetup(BaseModel):
    wallet_address: str

class TransferSettings(BaseModel):
    mode: str
    min_threshold_usd: float = 1000.0
    min_threshold_eth: float = 0.5
    transfer_percentage: int = 50
    auto_transfer_enabled: bool = False

class ManualTransfer(BaseModel):
    percentage: int
    current_balance_eth: float

@router.post("/setup-wallet")
async def setup_destination_wallet(wallet: WalletSetup):
    """Set destination wallet from MetaMask connection"""
    result = await withdrawal_engine.set_destination_wallet(wallet.wallet_address)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.post("/transfer-settings")
async def update_transfer_settings(settings: TransferSettings):
    """Update transfer settings - slider values come via API"""
    try:
        mode = TransferMode(settings.mode)
        result = await withdrawal_engine.set_transfer_mode(mode, {
            'min_threshold_usd': settings.min_threshold_usd,
            'min_threshold_eth': settings.min_threshold_eth,
            'transfer_percentage': settings.transfer_percentage,
            'auto_transfer_enabled': settings.auto_transfer_enabled
        })
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid transfer mode: {e}")

@router.post("/manual-transfer")
async def execute_manual_transfer(transfer: ManualTransfer):
    """Execute manual transfer with percentage"""
    result = await withdrawal_engine.execute_manual_transfer(
        transfer.percentage, 
        transfer.current_balance_eth
    )
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.get("/check-auto-transfer")
async def check_auto_transfer_conditions(current_profit_eth: float):
    """Check auto transfer conditions"""
    return await withdrawal_engine.check_auto_transfer_conditions(current_profit_eth)

@router.get("/status")
async def get_withdrawal_status():
    """Get current withdrawal system status"""
    return await withdrawal_engine.get_withdrawal_status()

@router.get("/metamask-integration")
async def get_metamask_integration_guide():
    """Provide MetaMask integration guide for external frontends"""
    return {
        "integration_type": "backend_api",
        "frontend_requirement": "external_only",
        "connection_flow": [
            "1. User connects MetaMask in their browser",
            "2. Frontend gets wallet address via window.ethereum",
            "3. Frontend calls /api/profit/setup-wallet with address",
            "4. Backend stores wallet for future transfers",
            "5. All transfers executed via backend APIs"
        ],
        "available_endpoints": [
            "POST /api/profit/setup-wallet",
            "POST /api/profit/transfer-settings", 
            "POST /api/profit/manual-transfer",
            "GET /api/profit/check-auto-transfer",
            "GET /api/profit/status"
        ],
        "contamination_status": "zero_frontend_files"
    }
