import React, { createContext, useContext, useState } from 'react';
const WalletContext = createContext();
export const useWallet = () => {
  const context = useContext(WalletContext);
  if (!context) {
    throw new Error('useWallet must be used within a WalletProvider');
  }
  return context;
};
export const WalletProvider = ({ children }) => {
  const [walletState, setWalletState] = useState({
    isConnected: false,
    account: null,
    chainId: null,
    balance: '0'
  });
  const value = { walletState, setWalletState };
  return (
    <WalletContext.Provider value={value}>
      {children}
    </WalletContext.Provider>
  );
};
