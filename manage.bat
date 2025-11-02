@echo off
echo í» ï¸  AI-NEXUS MANAGEMENT
echo ======================
echo 1. View Logs
echo 2. Restart Container
echo 3. Stop Container
echo 4. Deploy Fresh
echo.
choice /c 1234 /n /m "Select option:"

if errorlevel 4 goto deploy
if errorlevel 3 goto stop
if errorlevel 2 goto restart
if errorlevel 1 goto logs

:logs
docker logs -f ainexus-prod
goto end

:restart
docker restart ainexus-prod
echo âœ… Container restarted
goto end

:stop
docker stop ainexus-prod
echo í»‘ Container stopped
goto end

:deploy
docker stop ainexus-prod 2>nul
docker rm ainexus-prod 2>nul
docker build -t ainexus-industrial .
docker run -d --name ainexus-prod -p 8000:8000 ainexus-industrial
echo âœ… Fresh deployment complete
goto end

:end
pause
