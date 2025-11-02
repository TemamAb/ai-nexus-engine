# -*- coding: utf-8 -*-
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
import os
import asyncio
import random
from datetime import datetime, timedelta
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI(title="AI-Nexus")

class UserSettings(BaseModel):
    refresh_interval: int = 3
    reinvestment_rate: int = 75

class SimulationEngine:
    def __init__(self):
        self.virtual_capital = 100000000
        self.total_profit = 0.0
        self.reinvested_profit = 0.0
        self.completed_trades = []
        self.simulation_running = False
        self.user_settings = UserSettings()
        self.performance = {"total_trades": 0, "successful_trades": 0, "success_rate": 0.0, "profit_per_hour": 0.0}
        self.hourly_profits = []
    
    def calculate_hourly_metrics(self):
        if not self.completed_trades: return 0.0
        one_hour_ago = datetime.now() - timedelta(hours=1)
        recent_trades = [t for t in self.completed_trades if datetime.fromisoformat(t["timestamp"].replace('Z', '+00:00')) > one_hour_ago]
        hourly_profit = sum(t["profit"] for t in recent_trades)
        self.hourly_profits.append(hourly_profit)
        if len(self.hourly_profits) > 24: self.hourly_profits.pop(0)
        if self.hourly_profits: self.performance["profit_per_hour"] = sum(self.hourly_profits) / len(self.hourly_profits)
        return self.performance["profit_per_hour"]
    
    async def scan_opportunities(self):
        pairs = [("ETH-USDC", 0.012, 1500, "#00ff00"), ("WBTC-USDT", 0.015, 2800, "#0099ff"), ("LINK-ETH", 0.018, 900, "#ff00ff")]
        opportunities = []
        for pair, spread, profit, color in pairs:
            if random.random() > 0.3:
                current_spread = max(0.008, spread + random.uniform(-0.004, 0.004))
                current_profit = max(300, profit + random.uniform(-150, 250))
                opportunities.append({"pair": pair, "spread": current_spread, "profit": current_profit, "exchanges": ["uniswap_v3", "sushiswap"], "timestamp": datetime.now().isoformat(), "color": color})
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
            status, status_color = "completed", "#00ff00"
        else:
            profit, status, status_color = 0, "failed", "#ff4444"
        
        trade = {"id": f"trade_{datetime.now().timestamp()}", "pair": opportunity["pair"], "profit": profit, "status": status, "status_color": status_color, "timestamp": datetime.now().isoformat(), "color": opportunity["color"]}
        self.completed_trades.append(trade)
        self.performance["total_trades"] += 1
        self.performance["success_rate"] = (self.performance["successful_trades"] / self.performance["total_trades"] * 100) if self.performance["total_trades"] > 0 else 0
        self.calculate_hourly_metrics()
        return trade

sim_engine = SimulationEngine()

@app.get("/")
async def root(): return {"status": "AI-Nexus Operational", "phase": "1", "virtual_capital": sim_engine.virtual_capital, "dashboard": "/dashboard"}

@app.get("/dashboard")
async def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI-Nexus</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            :root {
                --bg-primary: #0b0b15; --bg-secondary: #141422; --bg-card: #1e1e2d; 
                --text-primary: #ffffff; --text-secondary: #8c8cae; --border-color: #2d2d3d;
                --success: #00ff00; --accent-blue: #0099ff; --warning: #ff9900; --danger: #ff4444;
            }
            body { font-family: 'Segoe UI', Tahoma, sans-serif; background: var(--bg-primary); color: var(--text-primary); margin: 0; padding: 12px; font-size: 13px; }
            .container { max-width: 1400px; margin: 0 auto; }
            .header { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; margin-bottom: 16px; text-align: center; }
            .header h1 { font-size: 1.4em; margin: 0; background: linear-gradient(90deg, var(--success), var(--accent-blue)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .header p { font-size: 0.9em; color: var(--text-secondary); margin: 4px 0 0 0; }
            .content-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; }
            .metrics-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px; }
            .metric-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; }
            .metric-card h3 { font-size: 0.8em; color: var(--text-secondary); margin: 0 0 8px 0; text-transform: uppercase; letter-spacing: 0.5px; }
            .metric-value { font-size: 1.6em; font-weight: 400; }
            .capital { color: var(--success); } .profit { color: var(--success); } .hourly { color: var(--accent-blue); } .reinvest { color: var(--warning); }
            .settings-panel { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; }
            .settings-panel h3 { font-size: 0.9em; color: var(--text-secondary); margin: 0 0 12px 0; }
            .setting-group { margin-bottom: 12px; }
            .setting-label { display: block; font-size: 0.8em; color: var(--text-secondary); margin-bottom: 4px; }
            select, input[type="range"] { width: 100%; background: var(--bg-secondary); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 4px; padding: 6px; font-size: 0.8em; }
            .slider-value { font-size: 0.9em; color: var(--accent-blue); text-align: center; margin-top: 4px; }
            .controls { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin: 12px 0; }
            .btn { background: var(--bg-secondary); border: 1px solid var(--border-color); color: var(--text-primary); padding: 8px 12px; border-radius: 4px; cursor: pointer; font-size: 0.8em; text-align: center; }
            .btn-primary { background: var(--success); color: black; }
            .panels-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
            .panel { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 12px; }
            .panel h3 { font-size: 0.9em; color: var(--text-secondary); margin: 0 0 8px 0; }
            .opportunity-item, .trade-item { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 4px; padding: 8px; margin-bottom: 6px; font-size: 0.8em; }
            .trade-success { border-left: 3px solid var(--success); }
            .trade-failed { border-left: 3px solid var(--danger); }
            .status { display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: var(--success); margin-right: 6px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>AI-Nexus $100M Engine</h1>
                <p>Phase 1 Simulation</p>
            </div>
            
            <div class="content-grid">
                <div>
                    <div class="metrics-grid">
                        <div class="metric-card">
                            <h3>Capital</h3>
                            <div class="metric-value capital" id="virtualCapital">$100.0M</div>
                        </div>
                        <div class="metric-card">
                            <h3>Profit</h3>
                            <div class="metric-value profit" id="totalProfit">$0.00</div>
                        </div>
                        <div class="metric-card">
                            <h3>$/Hour</h3>
                            <div class="metric-value hourly" id="profitPerHour">$0.00</div>
                        </div>
                        <div class="metric-card">
                            <h3>Reinvest</h3>
                            <div class="metric-value reinvest" id="reinvestmentRate">75%</div>
                        </div>
                    </div>
                    
                    <div class="panels-grid">
                        <div class="panel">
                            <h3>Opportunities</h3>
                            <div id="opportunitiesList">-</div>
                        </div>
                        <div class="panel">
                            <h3>Recent Trades</h3>
                            <div id="tradesList">-</div>
                        </div>
                    </div>
                </div>
                
                <div>
                    <div class="settings-panel">
                        <h3>Settings</h3>
                        <div class="setting-group">
                            <label class="setting-label">Refresh</label>
                            <select id="refreshInterval">
                                <option value="1000">1 sec</option>
                                <option value="2000">2 sec</option>
                                <option value="3000" selected>3 sec</option>
                                <option value="5000">5 sec</option>
                                <option value="10000">10 sec</option>
                            </select>
                        </div>
                        <div class="setting-group">
                            <label class="setting-label">Reinvest Rate</label>
                            <input type="range" min="1" max="100" value="75" id="reinvestmentSlider">
                            <div class="slider-value" id="reinvestmentValue">75%</div>
                        </div>
                    </div>
                    
                    <div class="controls">
                        <button class="btn btn-primary" onclick="startSimulation()">Start</button>
                        <button class="btn" onclick="stopSimulation()">Stop</button>
                        <button class="btn" onclick="scanOpportunities()">Scan</button>
                        <button class="btn" onclick="refreshMetrics()">Refresh</button>
                    </div>
                    
                    <div class="panel">
                        <h3>Performance</h3>
                        <div style="font-size: 0.8em;">
                            Trades: <span id="totalTrades">0</span> | 
                            Rate: <span id="successRate">0%</span> |
                            <span class="status"></span><span id="simStatus">Ready</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            let refreshTimer;
            let currentInterval = 3000;
            
            function updateRefreshInterval() {
                const select = document.getElementById('refreshInterval');
                currentInterval = parseInt(select.value);
                clearInterval(refreshTimer);
                refreshTimer = setInterval(refreshMetrics, currentInterval);
            }
            
            function updateReinvestmentRate(value) {
                document.getElementById('reinvestmentValue').textContent = value + '%';
                fetch('/api/settings/reinvestment', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({reinvestment_rate: parseInt(value)})
                });
            }
            
            async function startSimulation() {
                await fetch('/api/simulation/start', {method: 'POST'});
                document.getElementById('simStatus').textContent = 'Running';
                refreshMetrics();
            }
            
            async function stopSimulation() {
                await fetch('/api/simulation/stop', {method: 'POST'});
                document.getElementById('simStatus').textContent = 'Stopped';
                refreshMetrics();
            }
            
            async function scanOpportunities() {
                const response = await fetch('/api/opportunities');
                const data = await response.json();
                let html = '';
                data.opportunities.forEach(opp => {
                    html += `<div class="opportunity-item">${opp.pair} | ${(opp.spread*100).toFixed(2)}% | +$${opp.profit.toFixed(2)}</div>`;
                });
                document.getElementById('opportunitiesList').innerHTML = html || '-';
            }
            
            async function refreshMetrics() {
                const response = await fetch('/api/metrics');
                const data = await response.json();
                
                document.getElementById('totalProfit').textContent = '$' + data.total_profit.toFixed(2);
                document.getElementById('profitPerHour').textContent = '$' + data.performance.profit_per_hour.toFixed(2);
                document.getElementById('reinvestmentRate').textContent = data.user_settings.reinvestment_rate + '%';
                document.getElementById('totalTrades').textContent = data.performance.total_trades;
                document.getElementById('successRate').textContent = data.performance.success_rate.toFixed(1) + '%';
                
                // Update trades
                const tradesResponse = await fetch('/api/trades');
                const tradesData = await tradesResponse.json();
                let tradesHtml = '';
                tradesData.trades.slice(-5).reverse().forEach(trade => {
                    const cls = trade.status === 'completed' ? 'trade-success' : 'trade-failed';
                    tradesHtml += `<div class="trade-item ${cls}">${trade.pair} | $${trade.profit.toFixed(2)}</div>`;
                });
                document.getElementById('tradesList').innerHTML = tradesHtml || '-';
            }
            
            // Initialize
            document.getElementById('refreshInterval').addEventListener('change', updateRefreshInterval);
            document.getElementById('reinvestmentSlider').addEventListener('input', (e) => updateReinvestmentRate(e.target.value));
            refreshTimer = setInterval(refreshMetrics, currentInterval);
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
        return {"message": "Started", "status": "active"}
    return {"message": "Already running", "status": "active"}

@app.post("/api/simulation/stop")
async def stop_simulation():
    sim_engine.simulation_running = False
    return {"message": "Stopped", "total_profit": sim_engine.total_profit}

async def run_simulation():
    while sim_engine.simulation_running:
        try:
            opportunities = await sim_engine.scan_opportunities()
            for opp in opportunities:
                if opp["spread"] > 0.01: await sim_engine.execute_trade(opp)
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Simulation error: {e}")
            await asyncio.sleep(2)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
