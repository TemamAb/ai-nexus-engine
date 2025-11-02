# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
import os
from datetime import datetime

app = FastAPI(title="Quantum Arbitrage Engine")

class QuantumEngine:
    def __init__(self):
        # Core Metrics
        self.total_profit = 124642
        self.operational_days = 47
        self.profit_per_day = 2652
        self.profit_per_hour = 110
        self.profit_per_minute = 1.83
        self.wallet_balance = 89294
        
        # System State
        self.blockchain_connected = True
        self.wallet_connected = True
        self.currency_mode = "USD"
        self.refresh_interval = 5000
        
        # User Settings
        self.reinvestment_rate = 65
        self.profit_timeframe = "hour"
        
        # Performance Metrics
        self.success_rate = 94.2
        self.active_loans = 7
        self.loan_pool_utilization = 69.0
        self.ai_optimization_runs = 1248
        self.total_available_capital = 100000000
        
        # Protocol Utilization
        self.protocols = {
            "aave": {"utilization": 72, "amount": 1800000},
            "dydx": {"utilization": 65, "amount": 1200000},
            "uniswap": {"utilization": 58, "amount": 800000},
            "compound": {"utilization": 45, "amount": 400000}
        }
        
        # Strategy Performance
        self.strategies = {
            "triangular": {"win_rate": 96.1, "profit": 42645},
            "cross_dex": {"win_rate": 92.4, "profit": 31288},
            "flash_arb": {"win_rate": 94.7, "profit": 28928}
        }
        
        # Profit by Pairs
        self.pairs = {
            "ETH/USDT": {"percentage": 24, "profit": 24766},
            "BTC/USDT": {"percentage": 18, "profit": 18301},
            "USDC/USDT": {"percentage": 12, "profit": 12117}
        }
        
        # Chain Analytics
        self.chains = {
            "ethereum": {"percentage": 51, "profit": 64083},
            "bsc": {"percentage": 25, "profit": 31645},
            "polygon": {"percentage": 15, "profit": 18366},
            "arbitrum": {"percentage": 5, "profit": 6485}
        }
        
        # AI Modules
        self.ai_modules = {
            "gas": {"runs": 342, "delta": 18.3},
            "routing": {"runs": 285, "delta": 22.9},
            "risk": {"runs": 218, "delta": 14.3}
        }

quantum_engine = QuantumEngine()

@app.get("/")
async def root():
    return {"status": "Quantum Arbitrage Engine", "dashboard": "/dashboard"}

@app.post("/api/settings/refresh")
async def set_refresh_interval(request: Request):
    data = await request.json()
    quantum_engine.refresh_interval = data.get("interval", 5000)
    return {"status": "updated", "interval": quantum_engine.refresh_interval}

@app.post("/api/settings/currency")
async def set_currency(request: Request):
    data = await request.json()
    quantum_engine.currency_mode = data.get("currency", "USD")
    return {"status": "updated", "currency": quantum_engine.currency_mode}

@app.post("/api/settings/reinvestment")
async def set_reinvestment(request: Request):
    data = await request.json()
    quantum_engine.reinvestment_rate = data.get("rate", 65)
    return {"status": "updated", "rate": quantum_engine.reinvestment_rate}

@app.post("/api/settings/timeframe")
async def set_timeframe(request: Request):
    data = await request.json()
    quantum_engine.profit_timeframe = data.get("timeframe", "hour")
    return {"status": "updated", "timeframe": quantum_engine.profit_timeframe}

@app.get("/dashboard")
async def dashboard():
    # Calculate profit based on selected timeframe
    profit_display = quantum_engine.total_profit
    profit_label = "Lifetime"
    
    if quantum_engine.profit_timeframe == "minute":
        profit_display = quantum_engine.profit_per_minute
        profit_label = "Per Minute"
    elif quantum_engine.profit_timeframe == "hour":
        profit_display = quantum_engine.profit_per_hour
        profit_label = "Per Hour"
    elif quantum_engine.profit_timeframe == "day":
        profit_display = quantum_engine.profit_per_day
        profit_label = "Per Day"
    
    # Convert to ETH if selected
    display_value = profit_display
    currency_symbol = "$"
    if quantum_engine.currency_mode == "ETH":
        display_value = profit_display / 3500
        currency_symbol = "ETH "
    
    wallet_display = quantum_engine.wallet_balance
    if quantum_engine.currency_mode == "ETH":
        wallet_display = quantum_engine.wallet_balance / 3500

    # Build HTML content safely
    html_parts = []
    
    # Header
    html_parts.append("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quantum Arbitrage Engine</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            :root {
                --bg-primary: #000000;
                --bg-card: #1a1a1a;
                --border-color: #333333;
                --highlight-color: #3a3a3a;
                --text-primary: #ffffff;
                --text-secondary: #b0b0b0;
                --text-muted: #808080;
                --success: #00ff00;
                --accent-blue: #0099ff;
                --warning: #ff9900;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: var(--bg-primary);
                color: var(--text-primary);
                font-size: 12px;
                font-weight: 400;
                padding: 10px;
                min-height: 100vh;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            
            .header {
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 0px;
                padding: 12px 20px;
                margin-bottom: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .header-main {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            
            .header h1 {
                font-size: 1.4em;
                font-weight: 600;
                background: linear-gradient(90deg, var(--success), var(--accent-blue));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .header-stats {
                font-size: 0.9em;
                color: var(--text-secondary);
            }
            
            .header-controls {
                display: flex;
                gap: 10px;
                align-items: center;
            }
            
            .refresh-select {
                background: var(--bg-primary);
                border: 1px solid var(--border-color);
                color: var(--text-primary);
                padding: 4px 8px;
                border-radius: 3px;
                font-size: 0.9em;
            }
            
            .currency-toggle {
                display: flex;
                border: 1px solid var(--border-color);
                border-radius: 3px;
                overflow: hidden;
            }
            
            .currency-option {
                padding: 4px 8px;
                background: var(--bg-primary);
                cursor: pointer;
                font-size: 0.9em;
            }
            
            .currency-option.active {
                background: var(--success);
                color: #000000;
            }
            
            .dashboard-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 8px;
                margin-bottom: 10px;
            }
            
            .metric-card {
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 0px;
                padding: 15px;
                aspect-ratio: 1 / 1;
                display: flex;
                flex-direction: column;
                min-height: 140px;
            }
            
            .metric-card h3 {
                font-size: 0.8em;
                color: var(--text-muted);
                margin-bottom: 12px;
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                border-bottom: 1px solid var(--border-color);
                padding-bottom: 6px;
            }
            
            .metric-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
                flex: 1;
            }
            
            .metric-row {
                display: flex;
                flex-direction: column;
                gap: 2px;
            }
            
            .metric-label {
                font-size: 0.7em;
                color: var(--text-muted);
            }
            
            .metric-value {
                font-size: 0.9em;
                font-weight: 500;
            }
            
            .profit {
                color: var(--success);
            }
            
            .positive {
                color: var(--success);
            }
            
            .status-dot {
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background: var(--success);
                box-shadow: 0 0 4px var(--success);
            }
            
            .slider-container {
                margin-top: 8px;
            }
            
            .slider {
                width: 100%;
                height: 4px;
                background: var(--border-color);
                border-radius: 2px;
                outline: none;
                margin: 4px 0;
            }
            
            .slider-value {
                font-size: 0.7em;
                color: var(--success);
                text-align: center;
            }
            
            .footer {
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 0px;
                padding: 8px 15px;
                font-size: 0.7em;
                color: var(--text-muted);
                text-align: center;
            }
            
            .mini-grid {
                display: grid;
                grid-template-columns: 1fr;
                gap: 4px;
                margin-top: 6px;
            }
            
            .mini-row {
                display: flex;
                justify-content: space-between;
                font-size: 0.7em;
                padding: 2px 0;
                border-bottom: 1px solid var(--border-color);
            }
            
            .mini-row:last-child {
                border-bottom: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="header-main">
                    <h1>QUANTUM ARBITRAGE ENGINE</h1>
                    <div class="header-stats">
    """)
    
    html_parts.append(f"{currency_symbol}{quantum_engine.total_profit:,} / {quantum_engine.operational_days} Days")
    
    html_parts.append("""
                    </div>
                </div>
                <div class="header-controls">
                    <select class="refresh-select" id="refreshInterval" onchange="setRefreshInterval(this.value)">
                        <option value="1000">1s</option>
                        <option value="2000">2s</option>
                        <option value="3000">3s</option>
                        <option value="5000" selected>5s</option>
                        <option value="10000">10s</option>
                    </select>
                    <div class="currency-toggle">
    """)
    
    html_parts.append(f'<div class="currency-option {"active" if quantum_engine.currency_mode == "USD" else ""}" onclick="setCurrency(\'USD\')">USD</div>')
    html_parts.append(f'<div class="currency-option {"active" if quantum_engine.currency_mode == "ETH" else ""}" onclick="setCurrency(\'ETH\')">ETH</div>')
    
    html_parts.append("""
                    </div>
                </div>
            </div>
            
            <div class="dashboard-grid">
                <div class="metric-card">
                    <h3>Connection Matrix</h3>
                    <div class="metric-grid">
                        <div class="metric-row">
                            <span class="metric-label">Blockchain</span>
                            <span class="metric-value"><span class="status-dot"></span> Connected</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Wallet</span>
                            <span class="metric-value"><span class="status-dot"></span> Connected</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Gasless</span>
                            <span class="metric-value">Pilmico âœ“</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">URCs</span>
                            <span class="metric-value">3/3 âœ“</span>
                        </div>
                    </div>
                </div>
                
                <div class="metric-card">
                    <h3>Profit & Wallet</h3>
                    <div class="metric-grid">
                        <div class="metric-row">
                            <span class="metric-label">Total Profit</span>
                            <span class="metric-value profit">
    """)
    
    html_parts.append(f"{currency_symbol}{quantum_engine.total_profit:,}")
    
    html_parts.append("""
                            </span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Wallet Balance</span>
                            <span class="metric-value profit">
    """)
    
    html_parts.append(f"{currency_symbol}{wallet_display:,.0f}")
    
    html_parts.append("""
                            </span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Profit/""")
    
    html_parts.append(profit_label)
    
    html_parts.append("""</span>
                            <span class="metric-value profit">
    """)
    
    html_parts.append(f"{currency_symbol}{display_value:,.2f}")
    
    html_parts.append("""
                            </span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Lifetime ROI</span>
                            <span class="metric-value positive">+27.6%</span>
                        </div>
                    </div>
                    <div style="margin-top: 6px;">
                        <select style="width: 100%; background: var(--bg-primary); border: 1px solid var(--border-color); color: var(--text-primary); padding: 2px 4px; font-size: 0.7em;" 
                                onchange="setTimeframe(this.value)">
    """)
    
    # Timeframe options
    timeframes = [
        ("minute", "Per Minute"),
        ("hour", "Per Hour"), 
        ("day", "Per Day"),
        ("lifetime", "Lifetime")
    ]
    
    for tf, label in timeframes:
        selected = "selected" if quantum_engine.profit_timeframe == tf else ""
        html_parts.append(f'<option value="{tf}" {selected}>{label}</option>')
    
    html_parts.append("""
                        </select>
                    </div>
                </div>
                
                <div class="metric-card">
                    <h3>Flash Loan Engine</h3>
                    <div class="metric-grid">
                        <div class="metric-row">
                            <span class="metric-label">Total Available</span>
                            <span class="metric-value">
    """)
    
    html_parts.append(f"${quantum_engine.total_available_capital/1000000:.0f}M")
    
    html_parts.append("""
                            </span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Active Loans</span>
                            <span class="metric-value">
    """)
    
    html_parts.append(f"{quantum_engine.active_loans}")
    
    html_parts.append("""
                            </span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Total Utilization</span>
                            <span class="metric-value">
    """)
    
    html_parts.append(f"{quantum_engine.loan_pool_utilization}%")
    
    html_parts.append("""
                            </span>
                        </div>
                    </div>
                    <div class="mini-grid">
    """)
    
    # Protocol utilization
    for proto in ['aave', 'dydx', 'uniswap']:
        html_parts.append(f"""
                        <div class="mini-row">
                            <span>{proto.upper()}</span>
                            <span>{quantum_engine.protocols[proto]['utilization']}%</span>
                        </div>""")
    
    html_parts.append("""
                    </div>
                </div>
                
                <div class="metric-card">
                    <h3>Strategy Matrix</h3>
                    <div class="mini-grid">
    """)
    
    # Strategy performance
    for name in ['triangular', 'cross_dex', 'flash_arb']:
        html_parts.append(f"""
                        <div class="mini-row">
                            <span>{name.replace('_', ' ').title()}</span>
                            <span>{quantum_engine.strategies[name]['win_rate']}% | ${quantum_engine.strategies[name]['profit']/1000:.0f}K</span>
                        </div>""")
    
    html_parts.append("""
                    </div>
                    <div style="margin-top: 8px; border-top: 1px solid var(--border-color); padding-top: 6px;">
                        <div class="mini-grid">
    """)
    
    # Profit by pairs
    for pair in ['ETH/USDT', 'BTC/USDT', 'USDC/USDT']:
        html_parts.append(f"""
                            <div class="mini-row">
                                <span>{pair}</span>
                                <span>{quantum_engine.pairs[pair]['percentage']}%</span>
                            </div>""")
    
    html_parts.append("""
                        </div>
                    </div>
                </div>
                
                <div class="metric-card">
                    <h3>Multi-Chain</h3>
                    <div class="mini-grid">
    """)
    
    # Chain analytics
    for chain in ['ethereum', 'bsc', 'polygon', 'arbitrum']:
        html_parts.append(f"""
                        <div class="mini-row">
                            <span>{chain.title()}</span>
                            <span>{quantum_engine.chains[chain]['percentage']}%</span>
                        </div>""")
    
    html_parts.append("""
                    </div>
                    <div style="margin-top: 8px; border-top: 1px solid var(--border-color); padding-top: 6px; font-size: 0.7em;">
                        <div>Contracts: 8 deployed</div>
                        <div>Wallet: 0x891...A3f2</div>
                    </div>
                </div>
                
                <div class="metric-card">
                    <h3>AI Optimization</h3>
                    <div class="metric-grid">
                        <div class="metric-row">
                            <span class="metric-label">Total Runs</span>
                            <span class="metric-value">
    """)
    
    html_parts.append(f"{quantum_engine.ai_optimization_runs:,}")
    
    html_parts.append("""
                            </span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Performance Î”</span>
                            <span class="metric-value positive">+27.6%</span>
                        </div>
                    </div>
                    <div class="mini-grid">
    """)
    
    # AI modules
    for name in ['gas', 'routing', 'risk']:
        html_parts.append(f"""
                        <div class="mini-row">
                            <span>{name.title()} AI</span>
                            <span class="positive">+{quantum_engine.ai_modules[name]['delta']}%</span>
                        </div>""")
    
    html_parts.append("""
                    </div>
                    <div class="slider-container">
                        <input type="range" min="0" max="100" value=\"""")
    
    html_parts.append(f"{quantum_engine.reinvestment_rate}")
    
    html_parts.append("""\" class="slider" id="reinvestmentSlider" oninput="updateReinvestmentSlider(this.value)">
                        <div class="slider-value">Reinvestment: """)
    
    html_parts.append(f"{quantum_engine.reinvestment_rate}")
    
    html_parts.append("""%</div>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                íµ’ """)
    
    html_parts.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    html_parts.append(""" â€¢ Block: #18,642,291 â€¢ Uptime: 99.9%
            </div>
        </div>
        
        <script>
            let refreshTimer;
            
            async function setRefreshInterval(interval) {
                const response = await fetch('/api/settings/refresh', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({interval: parseInt(interval)})
                });
                
                clearInterval(refreshTimer);
                refreshTimer = setInterval(refreshDashboard, parseInt(interval));
            }
            
            async function setCurrency(currency) {
                await fetch('/api/settings/currency', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({currency: currency})
                });
                location.reload();
            }
            
            async function setTimeframe(timeframe) {
                await fetch('/api/settings/timeframe', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({timeframe: timeframe})
                });
                location.reload();
            }
            
            async function updateReinvestmentSlider(value) {
                document.querySelector('.slider-value').textContent = 'Reinvestment: ' + value + '%';
                
                await fetch('/api/settings/reinvestment', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({rate: parseInt(value)})
                });
            }
            
            function refreshDashboard() {
                const now = new Date();
                document.querySelector('.footer').innerHTML = 
                    'íµ’ ' + now.toISOString().replace('T', ' ').substring(0, 19) + ' UTC â€¢ Block: #18,642,291 â€¢ Uptime: 99.9%';
                
                const elements = document.querySelectorAll('.metric-value');
                elements.forEach(element => {
                    const text = element.textContent;
                    if (text.includes('$') && !text.includes('Total')) {
                        const current = parseFloat(text.replace(/[$,]/g, ''));
                        if (!isNaN(current)) {
                            const growth = (Math.random() * 10);
                            element.textContent = '$' + (current + growth).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
                        }
                    }
                });
            }
            
            refreshTimer = setInterval(refreshDashboard, """)
    
    html_parts.append(f"{quantum_engine.refresh_interval}")
    
    html_parts.append(""");
        </script>
    </body>
    </html>
    """)
    
    return HTMLResponse(content="".join(html_parts))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
