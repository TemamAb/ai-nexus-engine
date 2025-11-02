@echo off
if "%1"=="" (
    set /p port="Enter port (9000-9010): "
) else (
    set port=%1
)

echo íº€ Deploying AI-Nexus on port %port%
docker stop ainexus-port-%port% 2>nul
docker rm ainexus-port-%port% 2>nul
docker run -d --name ainexus-port-%port% -p %port%:%port% -e PORT=%port% ainexus-multi-port

echo âœ… Deployed on http://localhost:%port%
echo í³Š Health: http://localhost:%port%/health
