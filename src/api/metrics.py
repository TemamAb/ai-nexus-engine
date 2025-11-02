# coding: utf-8
"""
Prometheus Metrics - Monitoring endpoints for Grafana
Code Source: Prometheus Python client examples
"""
from prometheus_client import Counter, Histogram, generate_latest

# Metrics definitions
TRADES_EXECUTED = Counter('trades_executed_total', 'Total trades executed')
PROFIT_USD = Histogram('profit_usd', 'Profit in USD per trade')
EXECUTION_TIME = Histogram('execution_time_seconds', 'Trade execution time')

def get_metrics():
    return generate_latest()
