# Mainnet Configuration - Secure Environment Variables
import os

class MainnetConfig:
    # Blockchain Configuration
    ETH_MAINNET_RPC_URL = os.getenv('ETH_MAINNET_RPC_URL')
    DEPLOYER_ADDRESS = os.getenv('DEPLOYER_ADDRESS')
    
    # Gasless Configuration (Pilmico)
    PILMICO_API_KEY = os.getenv('PILMICO_API_KEY')
    PILMICO_URC_ADDRESS = os.getenv('PILMICO_URC_ADDRESS')
    
    # Protocol APIs
    AAVE_API_KEY = os.getenv('AAVE_API_KEY')
    UNISWAP_API_KEY = os.getenv('UNISWAP_API_KEY')
    
    # Mainnet Contract Addresses
    AAVE_V3_POOL = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2"
    UNISWAP_V3_ROUTER = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
    WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    
    @classmethod
    def validate_config(cls):
        required = ['ETH_MAINNET_RPC_URL', 'DEPLOYER_ADDRESS', 'PILMICO_API_KEY']
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise Exception(f"Missing required environment variables: {missing}")
        return True

# Validate configuration
try:
    MainnetConfig.validate_config()
    print("✅ MAINNET CONFIGURATION: VALID")
except Exception as e:
    print(f"❌ CONFIGURATION ERROR: {e}")
