#!/bin/bash

echo "=== AI-NEXUS DOCKER DEPLOYMENT ==="

# Build the Docker image
echo "Building Docker image..."
docker build -t ainexus-engine:latest .

# Run the container
echo "Starting AI-Nexus container..."
docker run -d \
  --name ainexus-engine \
  -p 8000:8000 \
  -e ETHEREUM_RPC="$ETHEREUM_RPC" \
  -e WALLET_ADDRESS="$WALLET_ADDRESS" \
  -e PIMLICO_API_KEY="$PIMLICO_API_KEY" \
  ainexus-engine:latest

echo "‚úÖ AI-Nexus Docker container running on port 8000"
echo "Ìºê Dashboard: http://localhost:8000"
echo "Ì¥ç Health check: http://localhost:8000/health"
