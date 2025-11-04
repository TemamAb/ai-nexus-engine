#!/bin/bash

echo "Ì¥ç AINEXUS PORT MONITOR"
echo "======================="

echo "Ì≥ä CURRENT PORT USAGE:"
echo "Port 8000 (FastAPI): $(netstat -tulpn 2>/dev/null | grep 8000 | wc -l) processes"
echo "Port 3000 (React): $(netstat -tulpn 2>/dev/null | grep 3000 | wc -l) processes"
echo "Port 5432 (PostgreSQL): $(netstat -tulpn 2>/dev/null | grep 5432 | wc -l) processes"
echo "Port 6379 (Redis): $(netstat -tulpn 2>/dev/null | grep 6379 | wc -l) processes"

echo ""
echo "Ì∞≥ DOCKER CONTAINERS:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo ""
echo "Ì∫Ä AINEXUS STATUS:"
if curl -s http://localhost:8000/health > /dev/null; then
    echo "‚úÖ AINEXUS ENGINE: RUNNING on http://localhost:8000"
    echo "Ì≤∞ Profit Target: \$250,000 daily"
    echo "Ì≤µ Capacity: \$100,000,000"
else
    echo "‚ùå AINEXUS ENGINE: NOT RUNNING"
fi
