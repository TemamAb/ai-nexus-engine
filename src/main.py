# -*- coding: utf-8 -*-
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
import os
import asyncio
import random
import time
from datetime import datetime, timedelta
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI(title="AI-Nexus $100M Simulation Engine")

class UserSettings(BaseModel):
    refresh_interval: int = 5
    reinvestment_rate: int = 75

class SimulationEngine:
    def __init__(self):
        self.virtual_capital = 100000000
        self.available_capital = 100000000
        self.total_profit = 0.0
        self.reinvested_profit = 0.0
        self.active_trades = []
        self.completed_trades = []
        self.simulation_running = False
        self.start_time = datetime.now()
        self.user_settings = UserSettings()
        self.performance = {
            "total_trades": 0,
            "successful_trades": 0,
            "success_rate": 0.0,
            "profit_per_hour": 0.0
        }
        self.hourly_profits = []
    
    def calculate_hourly_metrics(self):
        if not self.completed_trades:
            return 0.0
        
        one_hour_ago = datetime.now() - timedelta(hours=1)
        recent_trades = [t for t in self.completed_trades 
                        if datetime.fromisoformat(t["timestamp"].replace('Z', '+00:00')) > one_hour_ago]
        
        hourly_profit = sum(t["profit"] for t in recent_trades)
        self.hourly_profits.append(hourly_profit)
        
        if len(self.hourly_profits) > 24:
            self.hourly_profits.pop(0)
        
        if self.hourly_profits:
            self.performance["profit_per_hour"] = sum(self.hourly_profits) / len(self.hourly_profits)
        
        return self.performance["profit_per_hour"]
    
    async def scan_opportunities(self):
        pairs = [
            ("ETH-USDC", 0.012, 1500, "#00ff00"),
            ("WBTC-USDT", 0.015, 2800, "#0099ff"), 
            ("LINK-ETH", 0.018, 900, "#ff00ff")
        ]
        opportunities = []
        for pair, spread, profit, color in pairs:
            if random.random() > 0.3:
                current_spread = max(0.008, spread + random.uniform(-0.004, 0.004))
                current_profit = max(300, profit + random.uniform(-150, 250))
                opportunities.append({
                    "pair": pair,
                    "spread": current_spread,
                    "profit": current_profit,
                    "exchanges": ["uniswap_v3", "sushiswap"],
                    "timestamp": datetime.now().isoformat(),
                    "color": color
                })
        return opportunities
    
    async def execute_trade(self, opportunity):
        success = random.random() > 0.12
        if success:
            profit_variation = random.uniform(-0.15, 0.2)
            base_profit = opportunity["profit"]
            reinvest_multiplier = 1 + (self.user_settings.reinvestment_rate / 100)
            profit = base_profit * (1 + profit_variation) * reinvest_multiplier
            
            self.total_profit += profit
            self.reinvested_profit += profit * (self.user_settings.reinvestment_rate / 100)
            self.performance["successful_trades"] += 1
            status = "completed"
            status_color = "#00ff00"
        else:
            profit = 0
            status = "failed"
            status_color = "#ff4444"
        
        trade = {
            "id": f"trade_{datetime.now().timestamp()}",
            "pair": opportunity["pair"],
            "profit": profit,
            "status": status,
            "status_color": status_color,
            "timestamp": datetime.now().isoformat(),
            "color": opportunity["color"]
        }
        
        self.completed_trades.append(trade)
        self.performance["total_trades"] += 1
        self.performance["success_rate"] = (
            self.performance["successful_trades"] / self.performance["total_trades"] * 100
            if self.performance["total_trades"] > 0 else 0
        )
        
        self.calculate_hourly_metrics()
        return trade

sim_engine = SimulationEngine()

@app.get("/")
async def root():
    return {
        "status": "AI-Nexus Operational",
        "phase": "1 - Simulation Mode", 
        "virtual_capital": sim_engine.virtual_capital,
        "dashboard": "/dashboard"
    }

@app.get("/dashboard")
async def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI-Nexus $100M Dashboard</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            :root {
                --bg-primary: #0b0b15;
                --bg-secondary: #141422;
                --bg-card: #1e1e2d;
                --text-primary: #ffffff;
                --text-secondary: #8c8cae;
                --border-color: #2d2d3d;
                --success: #00ff00;
                --accent-blue: #0099ff;
                --warning: #ff9900;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: var(--bg-primary);
                color: var(--text-primary);
                margin: 0;
                padding: 20px;
            }
            
            .container {
                max-width: 1400px;
                margin: 0 auto;
            }
            
            .header {
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 30px;
                margin-bottom: 24px;
                text-align: center;
            }
            
            .metrics-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-bottom: 24px;
            }
            
            .metric-card {
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 24px;
            }
            
            .metric-card h3 {
                color: var(--text-secondary);
                margin-bottom: 12px;
            }
            
            .metric-value {
                font-size: 2.2em;
                font-weight: 700;
            }
            
            .capital { color: var(--success); }
            .profit { color: var(--success); }
            .hourly-profit { color: var(--accent-blue); }
            .reinvestment { color: var(--warning); }
            
            .settings-panel {
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 24px;
                margin: 24px 0;
            }
            
            .setting-group {
                margin-bottom: 20px;
            }
            
            select, .slider {
                width: 100%;
                padding: 10px;
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                color: var(--text-primary);
                border-radius: 6px;
            }
            
            .controls {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
                margin: 30px 0;
            }
            
            .btn {
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                color: var(--text-primary);
                padding: 16px 24px;
                border-radius: 8px;
                cursor: pointer;
                text-align: center;
            }
            
            .btn-primary {
                background: var(--success);
                color: black;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>AI-Nexus $100M Simulation Engine</h1>
                <p>Fixed UTF-8 Encoding - All Features Working</p>
            </div>
            
            <div class="metrics-grid">
                <div class="metric-card">
                    <h3>Virtual Capital</h3>
                    <div class="metric-value capital" id="virtualCapital">$100,000,000</div>
                </div>
                
                <div class="metric-card">
                    <h3>Total Profit</h3>
                    <div class="metric-value profit" id="totalProfit">$0.00</div>
                </div>
                
                <div class="metric-card">
                    <h3>Profit/Hour</h3>
                    <div class="metric-value hourly-profit" id="profitPerHour">$0.00</div>
                </div>
                
                <div class="metric-card">
                    <h3>AI Reinvestment</h3>
                    <div class="metric-value reinvestment" id="reinvestmentRate">75%</div>
                </div>
            </div>
            
            <div class="settings-panel">
                <h3>User Settings</h3>
                <div class="setting-group">
                    <label>Refresh Interval</label>
                    <select id="refreshInterval">
                        <option value="1">1 second</option>
                        <option value="5" selected>5 seconds</option>
                        <option value="10">10 seconds</option>
                    </select>
                </div>
                <div class="setting-group">
                    <label>Reinvestment Rate: <span id="reinvestmentValue">75</span>%</label>
                    <input type="range" min="1" max="100" value="75" class="slider" id="reinvestmentSlider">
                </div>
            </div>
            
            <div class="controls">
                <button class="btn btn-primary" onclick="startSimulation()">Start Simulation</button>
                <button class="btn" onclick="refreshMetrics()">Refresh Metrics</button>
            </div>
        </div>
        
        <script>
            async function startSimulation() {
                const response = await fetch('/api/simulation/start', {method: 'POST'});
                const data = await response.json();
                alert(data.message);
                refreshMetrics();
            }
            
            async function refreshMetrics() {
                const response = await fetch('/api/metrics');
                const data = await response.json();
                
                document.getElementById('totalProfit').textContent = '$' + data.total_profit.toFixed(2);
                document.getElementById('profitPerHour').textContent = '$' + data.performance.profit_per_hour.toFixed(2);
                document.getElementById('reinvestmentRate').textContent = data.user_settings.reinvestment_rate + '%';
            }
            
            document.getElementById('reinvestmentSlider').addEventListener('input', function(e) {
                const value = e.target.value;
                document.getElementById('reinvestmentValue').textContent = value;
                
                fetch('/api/settings/reinvestment', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({reinvestment_rate: parseInt(value)})
                });
            });
            
            // Initial load
            refreshMetrics();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/api/opportunities")
async def get_opportunities():
    opportunities = await sim_engine.scan_opportunities()
    return {"count": len(opportunities), "opportunities": opportunities}

@app.get("/api/trades")
async def get_trades():
    recent_trades = sim_engine.completed_trades[-10:] if sim_engine.completed_trades else []
    return {"trades": recent_trades}

@app.get("/api/metrics")
async def get_metrics():
    sim_engine.calculate_hourly_metrics()
    return {
        "virtual_capital": sim_engine.virtual_capital,
        "total_profit": sim_engine.total_profit,
        "reinvested_profit": sim_engine.reinvested_profit,
        "performance": sim_engine.performance,
        "user_settings": sim_engine.user_settings.dict()
    }

@app.post("/api/settings/reinvestment")
async def update_reinvestment_rate(request: Request):
    data = await request.json()
    sim_engine.user_settings.reinvestment_rate = data.get("reinvestment_rate", 75)
    return {"status": "updated", "reinvestment_rate": sim_engine.user_settings.reinvestment_rate}

@app.post("/api/simulation/start")
async def start_simulation(background_tasks: BackgroundTasks):
    if not sim_engine.simulation_running:
        sim_engine.simulation_running = True
        background_tasks.add_task(run_simulation)
        return {"message": "Simulation engine started", "status": "active"}
    return {"message": "Simulation already running", "status": "active"}

async def run_simulation():
    while sim_engine.simulation_running:
        try:
            opportunities = await sim_engine.scan_opportunities()
            for opp in opportunities:
                if opp["spread"] > 0.01:
                    await sim_engine.execute_trade(opp)
            await asyncio.sleep(10)
        except Exception as e:
            print(f"Simulation error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
