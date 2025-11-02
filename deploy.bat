@echo off
echo íº€ AI-NEXUS WINDOWS DEPLOYMENT
echo ==============================

docker --version >nul 2>&1
if errorlevel 1 (
    echo âŒ DOCKER NOT FOUND
    echo í²¡ Please install Docker Desktop first
    pause
    exit /b 1
)

echo âœ… DOCKER IS AVAILABLE
echo í³¦ BUILDING IMAGE...
docker build -t ainexus-industrial .

if errorlevel 1 (
    echo âŒ BUILD FAILED
    pause
    exit /b 1
)

echo âœ… BUILD SUCCESSFUL
echo í°³ STARTING CONTAINER...
docker run -d --name ainexus-prod -p 8000:8000 ainexus-industrial

echo.
echo âœ… DEPLOYMENT COMPLETE!
echo í¼ Access: http://localhost:8000
echo í³Š Health: http://localhost:8000/health
echo.
echo Press any key to view logs...
pause >nul
docker logs -f ainexus-prod
