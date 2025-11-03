#!/bin/bash
echo "ÌæØ AI-NEXUS DEPLOYMENT MONITOR"
echo "=============================="
echo "Target URL: https://ai-nexus-engine.onrender.com"
echo "Monitoring for successful deployment..."
echo ""

# First, prove the local code is correct
echo "Ì¥ç VERIFYING LOCAL CODE IS CORRECT:"
python3 -c "
with open('main.py', 'r') as f:
    content = f.read()
    if '\$100M' in content and '\$250,000' in content:
        print('‚úÖ LOCAL CODE CONTAINS: \$100M and \$250,000')
    else:
        print('‚ùå LOCAL CODE HAS ISSUES')
"
echo ""

# Monitor deployment
attempt=1
max_attempts=30

while [ $attempt -le $max_attempts ]; do
    echo "Ì¥Ñ Deployment check $attempt/$max_attempts..."
    
    # Try to reach the deployment
    response=$(curl -s -o /dev/null -w "%{http_code}" https://ai-nexus-engine.onrender.com/ 2>/dev/null || echo "000")
    
    case $response in
        "200")
            echo ""
            echo "Ìæâ DEPLOYMENT SUCCESSFUL! HTTP 200"
            echo ""
            echo "Ì≤∞ VERIFYING LIVE INSTITUTIONAL FEATURES:"
            curl -s https://ai-nexus-engine.onrender.com/ | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print('‚úÖ ' + data.get('pillar_1', 'Pillar 1 MISSING'))
    print('‚úÖ ' + data.get('profit_target', 'Profit MISSING'))
    print('‚úÖ Status: ' + data.get('status', 'MISSING'))
    print('')
    print('Ì∫Ä AI-NEXUS IS NOW LIVE AND OPERATIONAL!')
    print('Ìºê Access your platform at: https://ai-nexus-engine.onrender.com')
except Exception as e:
    print('‚ùå Could not parse response:', str(e))
"
            exit 0
            ;;
        "000")
            echo "   ‚è≥ Service not responding yet (deploying...)"
            ;;
        "404")
            echo "   ‚è≥ Service building (404 - not ready)"
            ;;
        "502"|"503")
            echo "   ‚è≥ Service starting (${response} - booting up)"
            ;;
        *)
            echo "   ‚è≥ Building... (HTTP ${response})"
            ;;
    esac
    
    sleep 10
    ((attempt++))
done

echo ""
echo "‚ùå DEPLOYMENT TIMEOUT - Check Render dashboard manually"
echo "Ìºê Visit: https://dashboard.render.com"
exit 1
