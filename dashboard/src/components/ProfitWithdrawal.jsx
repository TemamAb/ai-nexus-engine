import React, { useState } from 'react';
import useWithdrawal from '../hooks/useWithdrawal';

const ProfitWithdrawal = () => {
  const {
    connectedWallet,
    availableProfit,
    withdrawalConfig,
    updateWithdrawalConfig,
    executeWithdrawal,
    withdrawalHistory,
    isProcessing
  } = useWithdrawal();

  const [showConfig, setShowConfig] = useState(false);

  return (
    <div className="withdrawal-dashboard">
      <div className="section-header">
        <h2>Ì≤∞ Profit Withdrawal</h2>
        <button 
          className="config-toggle"
          onClick={() => setShowConfig(!showConfig)}
        >
          ‚öôÔ∏è Configuration
        </button>
      </div>

      {!connectedWallet ? (
        <div className="wallet-notice">
          <p>Connect your wallet to enable profit withdrawals</p>
        </div>
      ) : (
        <>
          <div className="withdrawal-overview">
            <div className="profit-card">
              <div className="label">Available for Withdrawal</div>
              <div className="amount">{availableProfit} ETH</div>
              <div className="usd-value">${(availableProfit * 3500).toLocaleString()} USD</div>
            </div>

            <button 
              className="withdraw-btn"
              onClick={executeWithdrawal}
              disabled={isProcessing || availableProfit === 0}
            >
              {isProcessing ? 'Processing...' : 'Withdraw Now'}
            </button>
          </div>

          {showConfig && (
            <div className="withdrawal-config">
              <h3>Auto-Withdrawal Settings</h3>
              
              <div className="config-item">
                <label>Threshold Amount (ETH)</label>
                <input
                  type="number"
                  value={withdrawalConfig.threshold}
                  onChange={(e) => updateWithdrawalConfig('threshold', e.target.value)}
                  step="0.1"
                  min="0.1"
                />
              </div>

              <div className="config-item">
                <label>Time Interval (Hours)</label>
                <input
                  type="range"
                  min="1"
                  max="72"
                  value={withdrawalConfig.interval}
                  onChange={(e) => updateWithdrawalConfig('interval', e.target.value)}
                />
                <span>{withdrawalConfig.interval} hours</span>
              </div>

              <div className="config-item">
                <label>
                  <input
                    type="checkbox"
                    checked={withdrawalConfig.autoWithdraw}
                    onChange={(e) => updateWithdrawalConfig('autoWithdraw', e.target.checked)}
                  />
                  Enable Auto-Withdrawal
                </label>
              </div>
            </div>
          )}

          <div className="withdrawal-history">
            <h3>Transfer History</h3>
            <div className="history-list">
              {withdrawalHistory.map((transfer, index) => (
                <div key={index} className="history-item">
                  <div className="transfer-info">
                    <span className="amount">{transfer.amount} ETH</span>
                    <span className="date">{transfer.date}</span>
                    <span className={`status ${transfer.status}`}>{transfer.status}</span>
                  </div>
                  <a href={transfer.txLink} target="_blank" rel="noopener noreferrer">
                    View Transaction
                  </a>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default ProfitWithdrawal;
