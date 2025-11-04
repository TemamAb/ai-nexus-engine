#!/bin/bash

echo "íº€ MANUAL AINEXUS START"
echo "======================="

# Stop existing
docker stop ainexus-engine 2>/dev/null
docker rm ainexus-engine 2>/dev/null

# Build fresh
docker build -t ainexus-engine:latest .

# Run with shell to manually start
docker run -it \
  --name ainexus-engine \
  -p 8000:8000 \
  -e ENVIRONMENT=production \
  ainexus-engine:latest \
  sh -c "cd src && python main.py"
