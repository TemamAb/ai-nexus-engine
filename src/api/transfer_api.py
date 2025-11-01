"""
Transfer Mode API Endpoints
Provides auto/manual mode control with slider settings
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.capital.transfer_manager import transfer_manager, TransferMode

router = APIRouter(prefix="/api/transfer", tags=["Transfer Modes"])

class TransferSettings(BaseModel):
    mode: str
    min_threshold_usd: float = 1000.0
    min_threshold_eth: float = 0.5
    transfer_percentage: int = 50
    auto_transfer_enabled: bool = False

class ManualTransferRequest(BaseModel):
    percentage: int
    current_balance_usd: float
    current_balance_eth: float

@router.get("/settings")
async def get_transfer_settings():
    """Get current transfer settings"""
    return transfer_manager.get_transfer_settings()

@router.post("/settings")
async def update_transfer_settings(settings: TransferSettings):
    """Update transfer settings with slider values"""
    try:
        mode = TransferMode(settings.mode)
        await transfer_manager.set_transfer_mode(mode, {
            'min_threshold_usd': settings.min_threshold_usd,
            'min_threshold_eth': settings.min_threshold_eth,
            'transfer_percentage': settings.transfer_percentage,
            'auto_transfer_enabled': settings.auto_transfer_enabled
        })
        return {"status": "success", "settings": transfer_manager.get_transfer_settings()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid transfer mode: {e}")

@router.post("/manual")
async def execute_manual_transfer(request: ManualTransferRequest):
    """Execute manual transfer with percentage slider"""
    if request.percentage < 1 or request.percentage > 100:
        raise HTTPException(status_code=400, detail="Percentage must be between 1 and 100")
    
    result = await transfer_manager.execute_manual_transfer(
        request.percentage,
        request.current_balance_usd,
        request.current_balance_eth
    )
    return result

@router.get("/check-auto")
async def check_auto_transfer_conditions(current_profit_usd: float, current_profit_eth: float):
    """Check if auto transfer conditions are met"""
    should_transfer = await transfer_manager.check_auto_transfer_conditions(
        current_profit_usd, current_profit_eth
    )
    return {
        "auto_transfer_conditions_met": should_transfer,
        "current_profit_usd": current_profit_usd,
        "current_profit_eth": current_profit_eth,
        "min_threshold_usd": transfer_manager.min_threshold_usd,
        "min_threshold_eth": transfer_manager.min_threshold_eth
    }
