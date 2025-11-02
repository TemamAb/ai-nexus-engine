#!/bin/bash
echo "Ì∫Ä SECURE MAINNET DEPLOYMENT USING RENDER ENV VARS"
echo "=================================================="

# Check for Render environment variables
echo "Checking environment variables..."

# Mainnet RPC URL from Render
if [ -n "$ETH_MAINNET_RPC_URL" ]; then
    echo "‚úÖ ETH_MAINNET_RPC_URL: Configured"
else
    echo "‚ùå ETH_MAINNET_RPC_URL: Not set in Render"
    echo "   Add in Render Dashboard: Environment Variables"
fi

# Wallet address (public) from Render
if [ -n "$DEPLOYER_ADDRESS" ]; then
    echo "‚úÖ DEPLOYER_ADDRESS: $DEPLOYER_ADDRESS"
else
    echo "‚ùå DEPLOYER_ADDRESS: Not set in Render"
fi

# Pilmico API Key from Render
if [ -n "$PILMICO_API_KEY" ]; then
    echo "‚úÖ PILMICO_API_KEY: Configured"
else
    echo "‚ùå PILMICO_API_KEY: Not set in Render"
fi

# Pilmico URC Address from Render
if [ -n "$PILMICO_URC_ADDRESS" ]; then
    echo "‚úÖ PILMICO_URC_ADDRESS: $PILMICO_URC_ADDRESS"
else
    echo "‚ùå PILMICO_URC_ADDRESS: Not set in Render"
fi

# Other API keys
if [ -n "$AAVE_API_KEY" ]; then
    echo "‚úÖ AAVE_API_KEY: Configured"
fi

if [ -n "$UNISWAP_API_KEY" ]; then
    echo "‚úÖ UNISWAP_API_KEY: Configured"
fi

echo ""
echo "Ì≥ã REQUIRED RENDER ENVIRONMENT VARIABLES:"
echo "   ETH_MAINNET_RPC_URL    - Mainnet RPC endpoint"
echo "   DEPLOYER_ADDRESS       - Your wallet address (public)"
echo "   PILMICO_API_KEY        - Gasless API key"
echo "   PILMICO_URC_ADDRESS    - Pilmico URC address"
echo "   AAVE_API_KEY           - Aave API access"
echo "   UNISWAP_API_KEY        - Uniswap API access"
echo ""
echo "Ì¥í SECURE APPROACH:"
echo "   - Private keys remain SECRET"
echo "   - Only public addresses in env vars"
echo "   - API keys managed by Render"
echo "   - Secure RPC endpoints"
echo ""
echo "Ì∫Ä To deploy: Add above variables in Render Dashboard"
echo "   Then restart deployment for mainnet activation"
