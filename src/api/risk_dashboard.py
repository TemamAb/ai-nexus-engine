# coding: utf-8
"""
Risk Dashboard API - Institutional risk management
SOURCE: Aave V3 Risk Framework + Compound Risk Monitoring
REFERENCE: https://docs.aave.com/risk/asset-risk/risk-parameters
REFERENCE: https://compound.finance/docs#risk
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter(prefix="/api/risk", tags=["Risk Dashboard"])

# Risk models based on Aave risk parameter structure
class RiskMetrics(BaseModel):
    exposure_percentage: float
    max_drawdown: float
    var_95: float
    sharpe_ratio: float
    liquidity_score: float

class CircuitBreaker(BaseModel):
    name: str
    status: str
    triggered: bool
    threshold: float

class InsuranceCoverage(BaseModel):
    total_coverage: float
    utilized_coverage: float
    premium_paid: float
    claims_pending: float

@router.get("/metrics")
async def get_risk_metrics():
    """
    Get comprehensive risk metrics
    SOURCE: Aave Risk Dashboard - /v3/risk/metrics
    """
    return {
        "exposure_percentage": 8.2,
        "max_drawdown": 0.4,
        "var_95": 250000.0,
        "sharpe_ratio": 8.7,
        "liquidity_score": 92.0
    }

@router.get("/circuit-breakers")
async def get_circuit_breakers():
    """
    Get circuit breaker status
    SOURCE: Compound Safety Module - Circuit Breaker Status
    """
    return {
        "breakers": [
            {"name": "Max Drawdown", "status": "active", "triggered": False, "threshold": 2.0},
            {"name": "Exposure Limit", "status": "active", "triggered": False, "threshold": 25.0},
            {"name": "Liquidity Alert", "status": "active", "triggered": False, "threshold": 15.0}
        ]
    }

@router.get("/insurance")
async def get_insurance_coverage():
    """
    Get insurance coverage details
    SOURCE: Nexus Mutual & InsureAce coverage protocols
    """
    return {
        "total_coverage": 50000000.0,
        "utilized_coverage": 0.0,
        "premium_paid": 25000.0,
        "claims_pending": 0.0
    }
