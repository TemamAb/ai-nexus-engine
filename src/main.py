# -*- coding: utf-8 -*-
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import asyncio
import random
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from pydantic import BaseModel

app = FastAPI(title="AI-Nexus $100M Simulation Engine")

class UserSettings(BaseModel):
    refresh_interval: int = 5
    reinvestment_rate: int = 75
    risk_tolerance: str = "medium"

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
            "daily_profit": 0.0,
            "hourly_profit": 0.0,
            "profit_per_hour": 0.0,
            "total_volume": 0.0
        }
        self.hourly_profits = []
    
    def calculate_hourly_metrics(self):
        """Calculate profit per hour metrics"""
        if not self.completed_trades:
            return 0.0
        
        # Calculate profit for last hour
        one_hour_ago = datetime.now() - timedelta(hours=1)
        recent_trades = [t for t in self.completed_trades 
                        if datetime.fromisoformat(t["timestamp"].replace('Z', '+00:00')) > one_hour_ago]
        
        hourly_profit = sum(t["profit"] for t in recent_trades)
        self.hourly_profits.append(hourly_profit)
        
        # Keep only last 24 hours
        if len(self.hourly_profits) > 24:
            self.hourly_profits.pop(0)
        
        # Calculate average profit per hour
        if self.hourly_profits:
            self.performance["profit_per_hour"] = sum(self.hourly_profits) / len(self.hourly_profits)
        
        return self.performance["profit_per_hour"]
    
    async def scan_opportunities(self):
        pairs = [
            ("ETH-USDC", 0.012, 1500, "#00ff00"),
            ("WBTC-USDT", 0.015, 2800, "#0099ff"), 
            ("LINK-ETH", 0.018, 900, "#ff00ff"),
            ("MATIC-USDC", 0.011, 650, "#ff9900"),
            ("AVAX-ETH", 0.014, 1200, "#e84142")
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
                    "color": color,
                    "volume": current_profit * random.randint(80, 150)
                })
        return opportunities
    
    async def execute_trade(self, opportunity):
        success = random.random() > 0.12  # 88% success rate
        if success:
            profit_variation = random.uniform(-0.15, 0.2)
            base_profit = opportunity["profit"]
            
            # Apply reinvestment multiplier
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
        
        # Update hourly metrics
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
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI-Nexus $100M Dashboard</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            :root {{
                --bg-primary: #0b0b15;
                --bg-secondary: #141422;
                --bg-card: #1e1e2d;
                --bg-hover: #252538;
                --text-primary: #ffffff;
                --text-secondary: #8c8cae;
                --text-muted: #666687;
                --border-color: #2d2d3d;
                --success: #00ff00;
                --warning: #ff9900;
                --danger: #ff4444;
                --accent-blue: #0099ff;
                --accent-purple: #9966ff;
            }}
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: var(--bg-primary);
                color: var(--text-primary);
                min-height: 100vh;
                line-height: 1.6;
            }}
            
            .container {{
                max-width: 1400px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            .header {{
                background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-card) 100%);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 30px;
                margin-bottom: 24px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }}
            
            .header h1 {{
                font-size: 2.5em;
                background: linear-gradient(90deg, var(--success), var(--accent-blue));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 8px;
            }}
            
            .header p {{
                color: var(--text-secondary);
                font-size: 1.1em;
            }}
            
            .metrics-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-bottom: 24px;
            }}
            
            .metric-card {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 24px;
                transition: all 0.3s ease;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
            }}
            
            .metric-card:hover {{
                background: var(--bg-hover);
                transform: translateY(-2px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }}
            
            .metric-card h3 {{
                color: var(--text-secondary);
                font-size: 0.9em;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                margin-bottom: 12px;
            }}
            
            .metric-value {{
                font-size: 2.2em;
                font-weight: 700;
                margin-bottom: 8px;
            }}
            
            .metric-change {{
                font-size: 0.9em;
                color: var(--success);
            }}
            
            .capital {{ color: var(--success); font-size: 2.5em; }}
            .profit {{ color: var(--success); font-size: 2.2em; }}
            .hourly-profit {{ color: var(--accent-blue); font-size: 2.2em; }}
            .success-rate {{ color: var(--accent-blue); font-size: 2.2em; }}
            .trades-count {{ color: var(--accent-purple); font-size: 2.2em; }}
            .reinvestment {{ color: var(--warning); font-size: 2.2em; }}
            
            .controls {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
                margin: 30px 0;
            }}
            
            .btn {{
                background: linear-gradient(135deg, var(--bg-secondary), var(--bg-card));
                border: 1px solid var(--border-color);
                color: var(--text-primary);
                padding: 16px 24px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 1em;
                font-weight: 600;
                transition: all 0.3s ease;
                text-align: center;
            }}
            
            .btn:hover {{
                background: linear-gradient(135deg, var(--bg-hover), var(--bg-card));
                border-color: var(--accent-blue);
                transform: translateY(-2px);
            }}
            
            .btn-primary {{
                background: linear-gradient(135deg, var(--success), #00cc00);
                border-color: var(--success);
            }}
            
            .btn-danger {{
                background: linear-gradient(135deg, var(--danger), #cc0000);
                border-color: var(--danger);
            }}
            
            .settings-panel {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 24px;
                margin: 24px 0;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
            }}
            
            .settings-panel h2 {{
                color: var(--text-secondary);
                font-size: 1.2em;
                margin-bottom: 20px;
                border-bottom: 1px solid var(--border-color);
                padding-bottom: 12px;
            }}
            
            .setting-group {{
                margin-bottom: 20px;
            }}
            
            .setting-label {{
                display: block;
                color: var(--text-secondary);
                margin-bottom: 8px;
                font-weight: 600;
            }}
            
            .slider-container {{
                background: var(--bg-secondary);
                border-radius: 8px;
                padding: 16px;
                margin: 10px 0;
            }}
            
            .slider {{
                width: 100%;
                height: 6px;
                border-radius: 3px;
                background: var(--border-color);
                outline: none;
                margin: 10px 0;
            }}
            
            .slider-value {{
                color: var(--accent-blue);
                font-weight: bold;
                font-size: 1.1em;
            }}
            
            select {{
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                color: var(--text-primary);
                padding: 10px 16px;
                border-radius: 6px;
                width: 100%;
                font-size: 1em;
            }}
            
            select:focus {{
                border-color: var(--accent-blue);
                outline: none;
            }}
            
            .content-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 24px;
                margin-top: 24px;
            }}
            
            .panel {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 24px;
                box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
            }}
            
            .panel h2 {{
                color: var(--text-secondary);
                font-size: 1.2em;
                margin-bottom: 20px;
                border-bottom: 1px solid var(--border-color);
                padding-bottom: 12px;
            }}
            
            .opportunity-item {{
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                border-radius: 8px;
                padding: 16px;
                margin-bottom: 12px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: all 0.3s ease;
            }}
            
            .opportunity-item:hover {{
                background: var(--bg-hover);
                border-color: var(--accent-blue);
            }}
            
            .trade-item {{
                background: var(--bg-secondary);
                border-left: 4px solid;
                border-radius: 6px;
                padding: 12px 16px;
                margin-bottom: 8px;
                font-size: 0.9em;
            }}
            
            .trade-success {{ border-left-color: var(--success); }}
            .trade-failed {{ border-left-color: var(--danger); }}
            
            .sparkline {{
                height: 40px;
                background: var(--bg-secondary);
                border-radius: 6px;
                margin-top: 8px;
                position: relative;
                overflow: hidden;
            }}
            
            .sparkline-fill {{
                height: 100%;
                background: linear-gradient(90deg, var(--success), var(--accent-blue));
                border-radius: 6px;
            }}
            
            .status-indicator {{
                display: inline-block;
                width: 8px;
                height: 8px;
                border-radius: 50%;
                margin-right: 8px;
            }}
            
            .status-active {{ background: var(--success); box-shadow: 0 0 8px var(--success); }}
            .status-inactive {{ background: var(--danger); }}
            
            .notification {{
                position: fixed;
                top: 20px;
                right: 20px;
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 8px;
                padding: 16px;
                color: var(--text-primary);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
                z-index: 1000;
                max-width: 300px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header -->
            <div class="header">
                <h1>Ì∫Ä AI-Nexus $100M Arbitrage Engine</h1>
                <p>Real-time simulation with advanced metrics ‚Ä¢ User configurable settings ‚Ä¢ AI Optimization</p>
                <div style="margin-top: 16px;">
                    <span class="status-indicator status-active"></span>
                    <span style="color: var(--success);">LIVE</span>
                    <span style="color: var(--text-secondary); margin: 0 16px;">|</span>
                    <span>Phase 1: Simulation Mode</span>
                    <span style="color: var(--text-secondary); margin: 0 16px;">|</span>
                    <span>Last update: <span id="lastUpdateTime">{datetime.now().strftime('%H:%M:%S')}</span></span>
                </div>
            </div>
            
            <!-- Metrics Grid -->
            <div class="metrics-grid">
                <div class="metric-card">
                    <h3>Virtual Capital</h3>
                    <div class="metric-value capital">${sim_engine.virtual_capital:,}</div>
                    <div class="sparkline">
                        <div class="sparkline-fill" style="width: 100%"></div>
                    </div>
                </div>
                
                <div class="metric-card">
                    <h3>Total Profit</h3>
                    <div class="metric-value profit" id="totalProfit">${sim_engine.total_profit:,.2f}</div>
                    <div class="metric-change" id="roiDisplay">+{(sim_engine.total_profit/sim_engine.virtual_capital*10000):.4f}% ROI</div>
                </div>
                
                <div class="metric-card">
                    <h3>Profit/Hour</h3>
                    <div class="metric-value hourly-profit" id="profitPerHour">${sim_engine.performance['profit_per_hour']:,.2f}</div>
                    <div class="metric-change" id="hourlyRate">Avg last 24h</div>
                </div>
                
                <div class="metric-card">
                    <h3>Success Rate</h3>
                    <div class="metric-value success-rate" id="successRate">{sim_engine.performance['success_rate']:.1f}%</div>
                    <div class="metric-change" id="successBreakdown">{sim_engine.performance['successful_trades']} / {sim_engine.performance['total_trades']} trades</div>
                </div>
                
                <div class="metric-card">
                    <h3>AI Reinvestment</h3>
                    <div class="metric-value reinvestment" id="reinvestmentRate">{sim_engine.user_settings.reinvestment_rate}%</div>
                    <div class="metric-change" id="reinvestedAmount">${sim_engine.reinvested_profit:,.2f} compounded</div>
                </div>
            </div>
            
            <!-- User Settings Panel -->
            <div class="settings-panel">
                <h2>‚öôÔ∏è User Settings & AI Optimization</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                    <div class="setting-group">
                        <label class="setting-label">Ì¥Ñ Refresh Interval</label>
                        <select id="refreshInterval" onchange="updateRefreshInterval()">
                            <option value="1">1 second</option>
                            <option value="2">2 seconds</option>
                            <option value="3">3 seconds</option>
                            <option value="5" selected>5 seconds</option>
                            <option value="10">10 seconds</option>
                        </select>
                        <div style="color: var(--text-muted); font-size: 0.9em; margin-top: 8px;">
                            Controls how often metrics update
                        </div>
                    </div>
                    
                    <div class="setting-group">
                        <label class="setting-label">ÌæØ AI Reinvestment Rate</label>
                        <div class="slider-container">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                                <span>1%</span>
                                <span class="slider-value" id="reinvestmentValue">{sim_engine.user_settings.reinvestment_rate}%</span>
                                <span>100%</span>
                            </div>
                            <input type="range" min="1" max="100" value="{sim_engine.user_settings.reinvestment_rate}" 
                                   class="slider" id="reinvestmentSlider" oninput="updateReinvestmentRate(this.value)">
                            <div style="color: var(--text-muted); font-size: 0.9em; margin-top: 8px;">
                                Percentage of profit automatically reinvested
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Controls -->
            <div class="controls">
                <button class="btn btn-primary" onclick="startSimulation()">Ì∫Ä Start Simulation</button>
                <button class="btn btn-danger" onclick="stopSimulation()">‚èπ Stop Engine</button>
                <button class="btn" onclick="scanOpportunities()">Ì¥ç Scan Opportunities</button>
                <button class="btn" onclick="refreshMetrics()">Ì¥Ñ Refresh Metrics</button>
                <button class="btn" onclick="viewTrades()">Ì≥ä Trade History</button>
            </div>
            
            <!-- Content Grid -->
            <div class="content-grid">
                <!-- Opportunities Panel -->
                <div class="panel">
                    <h2>ÌæØ Active Arbitrage Opportunities</h2>
                    <div id="opportunitiesList">
                        <div style="text-align: center; color: var(--text-muted); padding: 40px;">
                            Click "Scan Opportunities" to discover profitable trades
                        </div>
                    </div>
                </div>
                
                <!-- Recent Trades Panel -->
                <div class="panel">
                    <h2>‚ö° Recent Trade Execution</h2>
                    <div id="tradesList">
                        <div style="text-align: center; color: var(--text-muted); padding: 40px;">
                            No trades executed yet
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            let refreshInterval = 5000; // 5 seconds default
            let refreshTimer;
            
            function showNotification(message, type = 'info') {{
                const notification = document.createElement('div');
                notification.className = 'notification';
                notification.style.borderLeft = `4px solid ${{type === 'success' ? 'var(--success)' : type === 'error' ? 'var(--danger)' : 'var(--accent-blue)'}}`;
                notification.innerHTML = message;
                
                document.body.appendChild(notification);
                
                setTimeout(() => {{
                    notification.remove();
                }}, 3000);
            }}
            
            function updateRefreshInterval() {{
                const select = document.getElementById('refreshInterval');
                const interval = parseInt(select.value) * 1000;
                refreshInterval = interval;
                
                // Restart auto-refresh with new interval
                clearInterval(refreshTimer);
                refreshTimer = setInterval(refreshMetrics, refreshInterval);
                
                showNotification(`Ì¥Ñ Refresh interval set to ${{interval/1000}} seconds`, 'info');
            }}
            
            function updateReinvestmentRate(value) {{
                document.getElementById('reinvestmentValue').textContent = value + '%';
                
                // Send update to server
                fetch('/api/settings/reinvestment', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ reinvestment_rate: parseInt(value) }})
                }}).then(response => response.json())
                  .then(data => {{
                      document.getElementById('reinvestmentRate').textContent = value + '%';
                      showNotification(`ÌæØ Reinvestment rate updated to ${{value}}%`, 'success');
                  }});
            }}
            
            async function startSimulation() {{
                showNotification('Ì∫Ä Starting AI-Nexus simulation engine...', 'info');
                try {{
                    const response = await fetch('/api/simulation/start', {{method: 'POST'}});
                    const data = await response.json();
                    showNotification(`‚úÖ ${{data.message}}`, 'success');
                    refreshMetrics();
                    // Auto-refresh opportunities when simulation starts
                    setInterval(scanOpportunities, 10000);
                }} catch (error) {{
                    showNotification('‚ùå Failed to start simulation', 'error');
                }}
            }}
            
            async function stopSimulation() {{
                showNotification('‚èπ Stopping simulation engine...', 'warning');
                try {{
                    const response = await fetch('/api/simulation/stop', {{method: 'POST'}});
                    const data = await response.json();
                    showNotification(`Ìªë Simulation stopped. Final profit: $${{(data.total_profit || 0).toFixed(2)}}`, 'info');
                    refreshMetrics();
                }} catch (error) {{
                    showNotification('‚ùå Failed to stop simulation', 'error');
                }}
            }}
            
            async function scanOpportunities() {{
                try {{
                    const response = await fetch('/api/opportunities');
                    const data = await response.json();
                    
                    let html = '';
                    if (data.opportunities && data.opportunities.length > 0) {{
                        data.opportunities.forEach(opp => {{
                            html += `
                                <div class="opportunity-item">
                                    <div>
                                        <strong style="color: ${{opp.color}};">${{opp.pair}}</strong>
                                        <div style="font-size: 0.8em; color: var(--text-secondary);">
                                            ${{opp.exchanges[0]}} ‚Üî ${{opp.exchanges[1]}}
                                        </div>
                                    </div>
                                    <div style="text-align: right;">
                                        <div style="color: var(--success); font-weight: bold;">
                                            +$${{opp.profit.toFixed(2)}}
                                        </div>
                                        <div style="font-size: 0.8em; color: var(--text-secondary);">
                                            Spread: ${{(opp.spread * 100).toFixed(2)}}%
                                        </div>
                                    </div>
                                </div>
                            `;
                        }});
                    }} else {{
                        html = '<div style="text-align: center; color: var(--text-muted); padding: 20px;">No profitable opportunities found</div>';
                    }}
                    document.getElementById('opportunitiesList').innerHTML = html;
                    
                }} catch (error) {{
                    console.error('Error scanning opportunities:', error);
                }}
            }}
            
            async function viewTrades() {{
                try {{
                    const response = await fetch('/api/trades');
                    const data = await response.json();
                    
                    let html = '';
                    if (data.trades && data.trades.length > 0) {{
                        data.trades.slice(-8).reverse().forEach(trade => {{
                            const time = new Date(trade.timestamp).toLocaleTimeString();
                            const tradeClass = trade.status === 'completed' ? 'trade-success' : 'trade-failed';
                            html += `
                                <div class="trade-item ${{tradeClass}}">
                                    <div style="display: flex; justify-content: space-between;">
                                        <span style="color: ${{trade.color}};"><strong>${{trade.pair}}</strong></span>
                                        <span style="color: ${{trade.status_color}};"><strong>${{trade.status.toUpperCase()}}</strong></span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; font-size: 0.85em; margin-top: 4px;">
                                        <span>${{time}}</span>
                                        <span style="color: ${{trade.status_color}};">${{trade.profit > 0 ? '+' : ''}}$${{trade.profit.toFixed(2)}}</span>
                                    </div>
                                </div>
                            `;
                        }});
                    }} else {{
                        html = '<div style="text-align: center; color: var(--text-muted); padding: 20px;">No trades executed yet</div>';
                    }}
                    document.getElementById('tradesList').innerHTML = html;
                    
                }} catch (error) {{
                    console.error('Error loading trades:', error);
                }}
            }}
            
            async function refreshMetrics() {{
                try {{
                    const response = await fetch('/api/metrics');
                    const data = await response.json();
                    
                    // Update metrics display
                    document.getElementById('totalProfit').textContent = '$' + data.total_profit.toFixed(2);
                    document.getElementById('profitPerHour').textContent = '$' + data.performance.profit_per_hour.toFixed(2);
                    document.getElementById('successRate').textContent = data.performance.success_rate.toFixed(1) + '%';
                    document.getElementById('reinvestmentRate').textContent = data.user_settings.reinvestment_rate + '%';
                    document.getElementById('reinvestedAmount').textContent = '$' + data.reinvested_profit.toFixed(2) + ' compounded';
                    
                    // Update success rate breakdown
                    document.getElementById('successBreakdown').textContent = 
                        `${{data.performance.successful_trades}} / ${{data.performance.total_trades}} trades`;
                    
                    // Update ROI
                    const roi = (data.total_profit / data.virtual_capital * 10000).toFixed(4);
                    document.getElementById('roiDisplay').textContent = '+' + roi + '% ROI';
                    
                    // Update last update time
                    document.getElementById('lastUpdateTime').textContent = new Date().toLocaleTimeString();
                    
                }} catch (error) {{
                    console.error('Error refreshing metrics:', error);
                }}
            }}
            
            // Initialize settings
            document.getElementById('refreshInterval').value = '5';
            document.getElementById('reinvestmentSlider').value = {sim_engine.user_settings.reinvestment_rate};
            
            // Start auto-refresh
            refreshTimer = setInterval(refreshMetrics, refreshInterval);
            
            // Initial load
            refreshMetrics();
        </script>
    </body>
    </html>
    """)

@app.get("/api/opportunities")
async def get_opportunities():
    opportunities = await sim_engine.scan_opportunities()
    return {"count": len(opportunities), "opportunities": opportunities}

@app.get("/api/trades")
async def get_trades():
    recent_trades = sim_engine.completed_trades[-20:] if sim_engine.completed_trades else []
    return {"trades": recent_trades}

@app.get("/api/metrics")
async def get_metrics():
    sim_engine.calculate_hourly_metrics()
    return {
        "virtual_capital": sim_engine.virtual_capital,
        "total_profit": sim_engine.total_profit,
        "reinvested_profit": sim_engine.reinvested_profit,
        "performance": sim_engine.performance,
        "user_settings": sim_engine.user_settings.dict(),
        "simulation_active": sim_engine.simulation_running
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
        return {"message": "Simulation engine started with $100M virtual capital", "status": "active"}
    return {"message": "Simulation already running", "status": "active"}

@app.post("/api/simulation/stop")
async def stop_simulation():
    sim_engine.simulation_running = False
    return {"message": "Simulation stopped", "total_profit": sim_engine.total_profit}

async def run_simulation():
    while sim_engine.simulation_running:
        try:
            opportunities = await sim_engine.scan_opportunities()
            for opp in opportunities:
                if opp["spread"] > 0.01:  # 1% threshold
                    await sim_engine.execute_trade(opp)
            await asyncio.sleep(10)  # Run every 10 seconds for active simulation
        except Exception as e:
            print(f"Simulation error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
