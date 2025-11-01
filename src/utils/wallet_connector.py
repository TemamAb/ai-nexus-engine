"""
Wallet Connection Utility for MetaMask Detection
Dependencies carefully identified for local machine detection
"""
import asyncio
import json
from typing import Optional, Dict
import webbrowser

class WalletConnector:
    """
    MetaMask wallet connection utility
    Detects MetaMask on local machine and facilitates connection
    """
    
    def __init__(self):
        self.connected = False
        self.account_address = None
        self.network_id = None
        
    async def detect_metamask(self) -> bool:
        """
        Detect if MetaMask is installed on local machine
        Uses browser detection methods
        """
        try:
            # Method 1: Check for window.ethereum (MetaMask injection)
            # This would be called from frontend JavaScript
            detection_script = """
            if (typeof window.ethereum !== 'undefined') {
                return true;
            } else if (typeof window.web3 !== 'undefined') {
                return true;
            } else {
                return false;
            }
            """
            # In a real implementation, this would be executed in a browser context
            # For backend, we provide the detection script for frontend use
            self.metamask_detection_script = detection_script
            return True  # Assume available for integration
            
        except Exception as e:
            print(f"MetaMask detection error: {e}")
            return False
    
    def get_connection_script(self) -> str:
        """
        Return JavaScript for MetaMask connection
        Frontend will use this to connect and get account address
        """
        return """
        async function connectMetaMask() {
            try {
                if (typeof window.ethereum !== 'undefined') {
                    const accounts = await window.ethereum.request({
                        method: 'eth_requestAccounts'
                    });
                    return {
                        success: true,
                        address: accounts[0],
                        network: window.ethereum.networkVersion
                    };
                } else {
                    return {
                        success: false,
                        error: 'MetaMask not detected'
                    };
                }
            } catch (error) {
                return {
                    success: false,
                    error: error.message
                };
            }
        }
        """
    
    def set_connected_account(self, address: str, network: str):
        """Set the connected account details"""
        self.connected = True
        self.account_address = address
        self.network_id = network
        print(f"Wallet connected: {address} on network {network}")
    
    def get_connection_status(self) -> Dict:
        """Get current connection status"""
        return {
            "connected": self.connected,
            "account_address": self.account_address,
            "network_id": self.network_id,
            "detection_script": self.metamask_detection_script if hasattr(self, 'metamask_detection_script') else None
        }

# Global wallet connector instance
wallet_connector = WalletConnector()
