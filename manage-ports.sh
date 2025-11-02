#!/bin/bash
echo "í¾¯ AI-NEXUS MULTI-PORT MANAGEMENT"
echo "================================"

PS3="Select option: "
options=("Start All Ports" "Stop All Ports" "Restart All Ports" "Check Health" "Deploy Single Port" "Quit")

select opt in "${options[@]}"
do
    case $opt in
        "Start All Ports")
            echo "Starting ports 9000-9010..."
            for port in {9000..9010}; do
                docker run -d --name "ainexus-port-$port" -p $port:$port -e PORT=$port ainexus-multi-port
            done
            ;;
        "Stop All Ports")
            echo "Stopping all ports..."
            docker stop $(docker ps -a -q --filter "name=ainexus-port") 2>/dev/null
            docker rm $(docker ps -a -q --filter "name=ainexus-port") 2>/dev/null
            ;;
        "Restart All Ports")
            echo "Restarting all ports..."
            docker stop $(docker ps -a -q --filter "name=ainexus-port") 2>/dev/null
            docker rm $(docker ps -a -q --filter "name=ainexus-port") 2>/dev/null
            sleep 3
            for port in {9000..9010}; do
                docker run -d --name "ainexus-port-$port" -p $port:$port -e PORT=$port ainexus-multi-port
            done
            ;;
        "Check Health")
            echo "Checking health..."
            for port in {9000..9010}; do
                if curl -s --connect-timeout 2 http://localhost:$port/health >/dev/null; then
                    echo "âœ… Port $port: HEALTHY"
                else
                    echo "âŒ Port $port: UNHEALTHY"
                fi
            done
            ;;
        "Deploy Single Port")
            read -p "Enter port number (9000-9010): " port
            docker stop "ainexus-port-$port" 2>/dev/null
            docker rm "ainexus-port-$port" 2>/dev/null
            docker run -d --name "ainexus-port-$port" -p $port:$port -e PORT=$port ainexus-multi-port
            echo "âœ… Deployed on port $port"
            ;;
        "Quit")
            break
            ;;
        *) echo "Invalid option";;
    esac
done
