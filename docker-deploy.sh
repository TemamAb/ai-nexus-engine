#!/bin/bash

echo "Ì∫Ä AINEXUS PRODUCTION DEPLOYMENT"
echo "================================"

# Build production image
echo "Ì∞≥ Building production image..."
docker build -t ainexus-engine:prod .

# Deploy with production compose
echo "Ì∫Ä Deploying production stack..."
docker-compose -f docker-compose.prod.yml up -d

echo ""
echo "‚úÖ DEPLOYMENT COMPLETE!"
echo ""
echo "Ì≥ä SERVICES:"
docker-compose -f docker-compose.prod.yml ps

echo ""
echo "Ì¥ç MONITORING:"
echo "   Logs: docker-compose -f docker-compose.prod.yml logs -f"
echo "   Stats: docker stats"
echo ""
echo "Ì≤∞ SYSTEM READY FOR $250K DAILY PROFIT OPERATIONS!"
