# coding: utf-8
"""
Simulation to Live Adapter - Converts simulated trades to live execution
Code Source: Custom Hummingbot + Web3.py pattern
"""
from typing import Dict

class SimToLiveAdapter:
    def __init__(self, risk_manager, live_executor):
        self.risk_manager = risk_manager
        self.live_executor = live_executor
    
    async def convert_and_execute(self, sim_trade: Dict) -> Dict:
        """Convert simulated trade to live execution with risk checks"""
        # Based on adapter pattern implementation
        risk_check = self.risk_manager.validate_trade(sim_trade)
        
        if not risk_check['approved']:
            return {
                'status': 'rejected',
                'reason': risk_check['reason'],
                'original_sim_trade': sim_trade
            }
        
        # Convert simulation format to live execution format
        live_trade = self._convert_format(sim_trade)
        
        # Execute live trade
        execution_result = await self.live_executor.execute_trade(live_trade)
        
        return {
            'status': 'executed' if execution_result['status'] == 'success' else 'failed',
            'execution_result': execution_result,
            'original_sim_trade': sim_trade
        }
    
    def _convert_format(self, sim_trade: Dict) -> Dict:
        """Convert simulation trade format to live execution format"""
        return {
            'symbol': sim_trade.get('symbol'),
            'side': sim_trade.get('side'),
            'amount': sim_trade.get('amount'),
            'price_limit': sim_trade.get('price') * 1.001,  # Add 0.1% buffer
            'order_type': 'limit'
        }
