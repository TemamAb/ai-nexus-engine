#!/bin/bash
echo "ï¿½ï¿½ DEPLOY VIA GITHUB + RENDER AUTO-DEPLOY"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "âŒ Not a git repository. Initializing git..."
    git init
    git add .
    git commit -m "Initial AI-Nexus deployment"
fi

# Add all files to git
git add .
git commit -m "Deploy AI-Nexus Simulation Engine" || true

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    echo "í³¦ Please create a GitHub repository first:"
    echo "   1. Go to https://github.com/new"
    echo "   2. Create repository: ai-nexus-simulation"
    echo "   3. Run: git remote add origin https://github.com/YOUR_USERNAME/ai-nexus-simulation.git"
    echo "   4. Run: git push -u origin main"
else
    echo "í³¤ Pushing to GitHub to trigger auto-deploy..."
    git push origin main
fi

echo "âœ… Push complete! Render will auto-deploy from GitHub."
echo "í´— Check deployments at: https://dashboard.render.com"
