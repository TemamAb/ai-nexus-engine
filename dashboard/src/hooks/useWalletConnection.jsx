import { useState, useEffect } from 'react';
const useWalletConnection = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [accounts, setAccounts] = useState([]);
  const [selectedAccount, setSelectedAccount] = useState('');
  const [isConnecting, setIsConnecting] = useState(false);
  const connectMetaMask = async () => {
    setIsConnecting(true);
    try {
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
        setAccounts(accounts.map(addr => ({ address: addr, balance: '2.5' })));
        setSelectedAccount(accounts[0]);
        setIsConnected(true);
      }
    } catch (error) {
      console.error('MetaMask connection failed:', error);
    }
    setIsConnecting(false);
  };
  const connectWalletConnect = async () => {
    console.log('WalletConnect integration');
  };
  useEffect(() => {
    if (window.ethereum?.selectedAddress) {
      setIsConnected(true);
      setSelectedAccount(window.ethereum.selectedAddress);
    }
  }, []);
  return { isConnected, accounts, selectedAccount, setSelectedAccount, connectMetaMask, connectWalletConnect, isConnecting };
};
export default useWalletConnection;
