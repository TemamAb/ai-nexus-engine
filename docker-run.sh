#!/bin/bash

echo "Ì∞≥ STARTING AINEXUS CONTAINER..."
echo "================================="

# Check if image exists
if ! docker images | grep -q "ainexus-engine"; then
    echo "‚ùå AINexus image not found. Building first..."
    ./docker-build.sh
fi

echo ""
echo "Ì∫Ä Starting services..."
docker-compose up -d

echo ""
echo "Ì≥ä Checking services..."
sleep 10
docker-compose ps

echo ""
echo "Ìºê AINexus Engine should be available at: http://localhost:8000"
echo "Ì≥à Dashboard: http://localhost:8000"
echo "‚ù§Ô∏è  Health: http://localhost:8000/health"
echo ""
echo "Ì≥ã To view logs: docker-compose logs -f ainexus-engine"
