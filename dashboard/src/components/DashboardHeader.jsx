import React from 'react';
import useRefreshInterval from '../hooks/useRefreshInterval';
import useCurrencyDisplay from '../hooks/useCurrencyDisplay';
import useProfitMetrics from '../hooks/useProfitMetrics';

const DashboardHeader = () => {
  const { refreshInterval, setRefreshInterval, lastUpdated } = useRefreshInterval();
  const { currency, toggleCurrency, exchangeRate } = useCurrencyDisplay();
  const { totalProfit, daysOperational, dailyAverage, projectedMonthly, currentDailyProfit } = useProfitMetrics();

  const dailyTarget = 250000;
  const progress = (currentDailyProfit / dailyTarget) * 100;

  return (
    <div className="dashboard-header">
      <div className="header-top">
        <h1>íº€ AINEXUS TRADING ENGINE <span>v2.0.1</span></h1>
        <div className="header-controls">
          <div className="refresh-controls">
            <span>í´„ Refresh:</span>
            <select 
              value={refreshInterval} 
              onChange={(e) => setRefreshInterval(Number(e.target.value))}
            >
              <option value="1000">1s í´´</option>
              <option value="3000">3s í¿¡</option>
              <option value="5000">5s í¿¢</option>
              <option value="10000">10s í´µ</option>
            </select>
            <button onClick={() => window.location.reload()}>Refresh Now</button>
          </div>
          <div className="currency-toggle">
            <span>Currency:</span>
            <button 
              className={currency === 'ETH' ? 'active' : ''}
              onClick={() => toggleCurrency('ETH')}
            >
              ETH
            </button>
            <button 
              className={currency === 'USD' ? 'active' : ''}
              onClick={() => toggleCurrency('USD')}
            >
              USD
            </button>
          </div>
        </div>
      </div>
      
      <div className="header-subtitle">
        Enterprise-Grade DeFi Arbitrage System - $100M Capacity | $250K Daily Target
      </div>

      {/* Profit Target Progress */}
      <div className="profit-target">
        <div className="target-header">
          <span>í¾¯ DAILY PROFIT TARGET</span>
          <span>${dailyTarget.toLocaleString()}</span>
        </div>
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{width: `${progress}%`}}
          >
            <span>${currentDailyProfit.toLocaleString()} / ${dailyTarget.toLocaleString()}</span>
          </div>
        </div>
        <div className="efficiency-metric">
          Capital Efficiency: {((currentDailyProfit / 100000000) * 100).toFixed(3)}% | Target: 0.25%
        </div>
      </div>

      <div className="profit-metrics">
        <div className="profit-card">
          <div className="profit-label">TOTAL PROFIT (Since Deployment)</div>
          <div className="profit-amount">
            {currency === 'USD' ? '$' : ''}{totalProfit.toLocaleString()}{currency === 'ETH' ? ' ETH' : ''}
          </div>
        </div>
        <div className="metrics-grid">
          <div className="metric">
            <span>í³… Days Operational:</span>
            <strong>{daysOperational} days</strong>
          </div>
          <div className="metric">
            <span>í³Š Daily Average:</span>
            <strong>{currency === 'USD' ? '$' : ''}{dailyAverage.toLocaleString()}{currency === 'ETH' ? ' ETH' : ''}</strong>
          </div>
          <div className="metric">
            <span>íº€ Projected Monthly:</span>
            <strong>{currency === 'USD' ? '$' : ''}{projectedMonthly.toLocaleString()}{currency === 'ETH' ? ' ETH' : ''}</strong>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardHeader;
