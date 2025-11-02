#!/bin/bash
echo "íº€ AI-NEXUS GITHUB AUTO-DEPLOYMENT"

# Install dependencies
echo "í³¦ Installing dependencies..."
pip install -r requirements.txt

# Initialize git if needed
if [ ! -d ".git" ]; then
    git init
    echo "âœ… Git initialized"
fi

# Add all files
git add .
git commit -m "Deploy AI-Nexus Simulation Engine v1.0" || true

echo "í¾¯ NEXT STEPS:"
echo "   1. Create GitHub repo: https://github.com/new"
echo "   2. Name: ai-nexus-simulation"
echo "   3. Run: git remote add origin https://github.com/YOUR_USERNAME/ai-nexus-simulation.git"
echo "   4. Run: git push -u origin main"
echo ""
echo "í³‹ Or run: ./deploy-via-github.sh"
echo "í³– See: manual-deploy.md for detailed instructions"
