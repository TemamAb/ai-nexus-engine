import React from 'react';
import useSystemMetrics from '../hooks/useSystemMetrics';

const LiveMetrics = () => {
  const { metrics, systemHealth, executionStats } = useSystemMetrics();

  return (
    <div className="live-metrics">
      <div className="metrics-grid">
        {/* Four Pillars Monitoring */}
        <div className="metric-card critical">
          <h3>âš¡ Flash Loan System</h3>
          <div className="metric-value">${metrics.flashLoanUtilization}M / $100M</div>
          <div className="metric-progress">
            <div 
              className="progress-bar" 
              style={{width: `${(metrics.flashLoanUtilization / 100) * 100}%`}}
            ></div>
          </div>
          <div className="metric-sub">Success Rate: {metrics.flashLoanSuccessRate}%</div>
        </div>

        <div className="metric-card high">
          <h3>í´¥ Gasless Mode</h3>
          <div className="metric-value">{metrics.gaslessTransactions} TX</div>
          <div className="metric-sub">Savings: ${metrics.gasSavings}</div>
        </div>

        <div className="metric-card critical">
          <h3>í¾¯ Three-Tier System</h3>
          <div className="metric-status">
            <span className={`status-dot ${systemHealth.scannerTier}`}></span> Scanner
            <span className={`status-dot ${systemHealth.relayerTier}`}></span> Relayer
            <span className={`status-dot ${systemHealth.orchestratorTier}`}></span> Orchestrator
          </div>
        </div>

        <div className="metric-card high">
          <h3>í·  AI Optimization</h3>
          <div className="metric-value">{metrics.aiImprovement}% Gain</div>
          <div className="metric-sub">Active Models: {metrics.activeModels}</div>
        </div>
      </div>

      {/* Execution Quality Metrics */}
      <div className="quality-metrics">
        <h3>í¾¯ Execution Quality (Target: $250K Daily)</h3>
        <div className="quality-grid">
          <div className="metric">
            <div className="metric-value">${executionStats.avgProfit}</div>
            <div className="metric-label">Avg Profit/Trade</div>
          </div>
          <div className="metric">
            <div className="metric-value">{executionStats.successRate}%</div>
            <div className="metric-label">Success Rate</div>
          </div>
          <div className="metric">
            <div className="metric-value">{executionStats.tradesToday}</div>
            <div className="metric-label">Trades Today</div>
          </div>
          <div className="metric">
            <div className="metric-value">{((executionStats.avgProfit * executionStats.tradesToday) / 250000 * 100).toFixed(1)}%</div>
            <div className="metric-label">Daily Target Progress</div>
          </div>
        </div>
      </div>

      {/* Capital Efficiency */}
      <div className="efficiency-stats">
        <h3>í²° Capital Efficiency</h3>
        <div className="stats-grid">
          <div className="stat">
            <div className="stat-value">{((executionStats.avgProfit * executionStats.tradesToday) / 100000000 * 100).toFixed(3)}%</div>
            <div className="stat-label">Current ROI</div>
          </div>
          <div className="stat">
            <div className="stat-value">0.25%</div>
            <div className="stat-label">Target ROI</div>
          </div>
          <div className="stat">
            <div className="stat-value">${(100000000 * 0.0025).toLocaleString()}</div>
            <div className="stat-label">Daily Target</div>
          </div>
          <div className="stat">
            <div className="stat-value">15-20</div>
            <div className="stat-label">Quality Trades Needed</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LiveMetrics;
