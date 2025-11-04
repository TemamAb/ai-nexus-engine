import React from 'react';
import useWalletConnection from '../hooks/useWalletConnection';

const WalletConnectModal = ({ isOpen, onClose }) => {
  const { 
    connectMetaMask, 
    connectWalletConnect, 
    accounts, 
    selectedAccount,
    setSelectedAccount,
    isConnecting 
  } = useWalletConnection();

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <div className="modal-header">
          <h2>Connect Wallet</h2>
          <button onClick={onClose}>Ã—</button>
        </div>
        
        <div className="wallet-options">
          <button 
            className="wallet-btn metamask" 
            onClick={connectMetaMask}
            disabled={isConnecting}
          >
            <span>í¶Š</span>
            MetaMask
          </button>
          
          <button 
            className="wallet-btn walletconnect" 
            onClick={connectWalletConnect}
            disabled={isConnecting}
          >
            <span>í´—</span>
            WalletConnect
          </button>
        </div>

        {accounts.length > 0 && (
          <div className="account-selection">
            <h3>Select Account:</h3>
            {accounts.map((account) => (
              <div 
                key={account.address}
                className={`account-item ${selectedAccount === account.address ? 'selected' : ''}`}
                onClick={() => setSelectedAccount(account.address)}
              >
                <div className="account-address">{account.address}</div>
                <div className="account-balance">{account.balance} ETH</div>
              </div>
            ))}
          </div>
        )}

        <div className="modal-footer">
          <button onClick={onClose} className="btn-secondary">Cancel</button>
          <button onClick={onClose} className="btn-primary" disabled={!selectedAccount}>
            Connect
          </button>
        </div>
      </div>
    </div>
  );
};

export default WalletConnectModal;
