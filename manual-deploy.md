# íº€ Manual Deployment Instructions

## 1. Connect GitHub to Render

1. Go to https://dashboard.render.com
2. Click "New +" â†’ "Web Service"
3. Connect your GitHub repository
4. Select "ai-nexus-simulation" repository
5. Configure settings:
   - **Name**: ai-nexus-simulation
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

## 2. Environment Variables in Render Dashboard

Add these environment variables:
- `DEPLOYMENT_MODE=simulation`
- `VIRTUAL_CAPITAL=100000000`
- `BLOCKCHAIN_NETWORK=mainnet-fork`

## 3. Auto-Deploy on Git Push

Render will automatically deploy when you push to main branch!

