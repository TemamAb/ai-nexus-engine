#!/bin/bash
echo "Ì∫Ä AI-NEXUS LINUX/MAC DEPLOYMENT"
echo "================================"

# Build and run
docker build -t ainexus-industrial . && \
docker run -d --name ainexus-prod -p 8000:8000 ainexus-industrial

echo "‚úÖ Deployment complete!"
echo "Ìºê Access: http://localhost:8000"
echo "Ì≥ä Health: http://localhost:8000/health"
