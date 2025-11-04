import React from 'react';
import DashboardHeader from './components/DashboardHeader';
import LiveMetrics from './components/LiveMetrics';
import ProfitWithdrawal from './components/ProfitWithdrawal';
import SystemControls from './components/SystemControls';
import WalletConnectModal from './components/WalletConnectModal';
import { WalletProvider } from './context/WalletContext';
import './index.css';

function App() {
  const [showWalletModal, setShowWalletModal] = React.useState(false);

  return (
    <WalletProvider>
      <div className="App">
        <DashboardHeader />
        
        <div className="dashboard-body">
          <div className="main-panel">
            <LiveMetrics />
            <ProfitWithdrawal />
          </div>
          
          <div className="sidebar">
            <SystemControls />
            <div className="wallet-section">
              <button 
                className="connect-wallet-btn"
                onClick={() => setShowWalletModal(true)}
              >
                Connect Wallet
              </button>
            </div>
          </div>
        </div>

        <WalletConnectModal 
          isOpen={showWalletModal}
          onClose={() => setShowWalletModal(false)}
        />
      </div>
    </WalletProvider>
  );
}

export default App;
