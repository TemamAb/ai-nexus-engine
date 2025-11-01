"""
AINEXUS Main Entry Point - Fixed for Render deployment
"""
import sys
import os

# Add src to Python path for proper imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from api.app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
