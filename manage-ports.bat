@echo off
echo í¾¯ AI-NEXUS MULTI-PORT MANAGEMENT
echo ================================
echo.
echo Running instances:
docker ps --filter "name=ainexus-port" --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"
echo.
echo 1. Start All Ports (9000-9010)
echo 2. Stop All Ports
echo 3. Restart All Ports
echo 4. Check Health All
echo 5. Deploy Single Port
echo.
set /p choice="Select option (1-5): "

if "%choice%"=="1" goto startall
if "%choice%"=="2" goto stopall
if "%choice%"=="3" goto restartall
if "%choice%"=="4" goto healthall
if "%choice%"=="5" goto singleport

:startall
echo Starting all ports 9000-9010...
for /l %%i in (9000,1,9010) do (
    echo Starting port %%i...
    docker run -d --name ainexus-port-%%i -p %%i:%%i -e PORT=%%i ainexus-multi-port 2>nul
)
goto end

:stopall
echo Stopping all ports...
docker stop $(docker ps -a -q --filter "name=ainexus-port") 2>nul
docker rm $(docker ps -a -q --filter "name=ainexus-port") 2>nul
goto end

:restartall
echo Restarting all ports...
docker stop $(docker ps -a -q --filter "name=ainexus-port") 2>nul
docker rm $(docker ps -a -q --filter "name=ainexus-port") 2>nul
timeout 3
for /l %%i in (9000,1,9010) do (
    docker run -d --name ainexus-port-%%i -p %%i:%%i -e PORT=%%i ainexus-multi-port 2>nul
)
goto end

:healthall
echo Checking health of all ports...
for /l %%i in (9000,1,9010) do (
    curl -s http://localhost:%%i/health >nul && (
        echo âœ… Port %%i: HEALTHY
    ) || (
        echo âŒ Port %%i: UNHEALTHY
    )
)
goto end

:singleport
set /p port="Enter port number (9000-9010): "
echo Deploying on port %port%...
docker stop ainexus-port-%port% 2>nul
docker rm ainexus-port-%port% 2>nul
docker run -d --name ainexus-port-%port% -p %port%:%port% -e PORT=%port% ainexus-multi-port
echo âœ… Deployed on port %port%
goto end

:end
echo.
pause
