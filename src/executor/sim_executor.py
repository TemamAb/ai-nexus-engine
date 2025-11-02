# coding: utf-8
"""
Simulation Executor - Sandbox trade execution
Code Source: Hummingbot backtesting scripts
"""
import pandas as pd
from typing import Dict

class SimExecutor:
    def __init__(self, initial_capital: float = 10000.0):
        self.capital = initial_capital
        self.positions = {}
        self.trade_history = []
    
    def execute_sim_trade(self, trade_signal: Dict) -> Dict:
        """Execute trade in simulation environment"""
        # Based on Hummingbot backtesting execution patterns
        symbol = trade_signal.get('symbol', 'ETH/USD')
        side = trade_signal.get('side', 'buy')
        amount = trade_signal.get('amount', 0)
        price = trade_signal.get('price', 0)
        
        if side == 'buy' and self.capital >= amount * price:
            # Simulate buy
            self.capital -= amount * price
            self.positions[symbol] = self.positions.get(symbol, 0) + amount
            profit = 0  # No profit on entry
        elif side == 'sell' and self.positions.get(symbol, 0) >= amount:
            # Simulate sell
            self.capital += amount * price
            self.positions[symbol] -= amount
            profit = amount * price * 0.002  # Mock 0.2% profit
        
        trade_result = {
            'symbol': symbol,
            'side': side,
            'amount': amount,
            'price': price,
            'profit': profit,
            'remaining_capital': self.capital
        }
        
        self.trade_history.append(trade_result)
        return trade_result
