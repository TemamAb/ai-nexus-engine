import os

print("Ì¥ç VERIFYING RENDER ENVIRONMENT CONFIGURATION")
print("=============================================")

# Check exact variable names from Render
variables = {
    "BLOCKCHAIN_RPC": [
        "ETHEREUM_RPC",
        "ARBITRUM_RPC", 
        "OPTIMISM_RPC",
        "BASE_RPC",
        "POLYGON_RPC"
    ],
    "GASLESS_INFRASTRUCTURE": [
        "BUNDLER_URL",
        "PAYMASTER_URL", 
        "PIMLICO_API_KEY",
        "ENTRYPOINT_ADDRESS"
    ],
    "WALLET_SECURITY": [
        "WALLET_ADDRESS"
    ],
    "FLASH_LOAN_PROVIDERS": [
        "AAVE_POOL_ADDRESS",
        "UNISWAP_V3_ROUTER"
    ],
    "AI_TRADING_PARAMETERS": [
        "MIN_PROFIT_THRESHOLD",
        "MAX_SINGLE_TRADE",
        "DAILY_LOSS_LIMIT"
    ]
}

print("Ì≥ã RENDER ENVIRONMENT STATUS:")
for category, vars_list in variables.items():
    print(f"\n{category}:")
    for var in vars_list:
        value = os.getenv(var)
        if value:
            if "KEY" in var or "URL" in var or "ADDRESS" in var:
                print(f"  ‚úÖ {var}: CONFIGURED")
            else:
                print(f"  ‚úÖ {var}: {value}")
        else:
            print(f"  ‚ùå {var}: NOT SET")

print("\nÔøΩÔøΩ DEPLOYMENT READINESS:")
required = ["ETHEREUM_RPC", "WALLET_ADDRESS"]
missing = [var for var in required if not os.getenv(var)]

if not missing:
    print("‚úÖ READY FOR SECURE MANUAL DEPLOYMENT")
    print("   All required variables configured")
else:
    print("ÔøΩÔ∏è  MISSING REQUIRED VARIABLES:")
    for var in missing:
        print(f"   - {var}")

print("\nÌ∫Ä NEXT STEP: Secure manual contract deployment")
print("   Will generate real blockchain proof:")
print("   - Contract addresses")
print("   - Transaction hashes") 
print("   - Block numbers")
print("   - Timestamps")
