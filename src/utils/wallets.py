# coding: utf-8
"""
Wallet Management - Multi-sig and transaction signing
Code Source: OpenZeppelin multi-sig examples, Web3.py signing
"""
from web3 import Web3
from eth_account import Account
from typing import List, Dict

class WalletManager:
    def __init__(self, provider_url: str):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.accounts = {}
    
    def add_account_from_private_key(self, private_key: str, label: str = "default") -> str:
        """Add account from private key"""
        # Based on Web3.py account management patterns
        account = self.w3.eth.account.from_key(private_key)
        self.accounts[label] = account
        return account.address
    
    def sign_transaction(self, transaction_dict: Dict, account_label: str = "default") -> Dict:
        """Sign transaction with specified account"""
        # Based on Web3.py transaction signing patterns
        if account_label not in self.accounts:
            raise ValueError(f"Account {account_label} not found")
        
        account = self.accounts[account_label]
        signed_tx = self.w3.eth.account.sign_transaction(transaction_dict, account.key)
        return signed_tx
    
    def get_balance(self, address: str = None, account_label: str = None) -> int:
        """Get balance for address or account"""
        if account_label:
            address = self.accounts[account_label].address
        return self.w3.eth.get_balance(address)
