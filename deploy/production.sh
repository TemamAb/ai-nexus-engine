#!/bin/bash
echo "Ì∫Ä AINEXUS Production Deployment"
echo "================================="

# Build production image
docker build -t ainexus-engine:prod .

# Deploy with docker-compose
docker-compose -f docker-compose.prod.yml up -d

echo "‚úÖ AINEXUS deployed to production"
echo "Ìºê API: http://localhost:8000"
echo "Ì≥ä Metrics: http://localhost:9090"
echo "Ì≥à Dashboard: http://localhost:3000 (admin/ainexus123)"
