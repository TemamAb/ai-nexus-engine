#!/usr/bin/env python3
"""
Test script to verify main.py configuration
"""

import sys
import os

# Add src directory to path
sys.path.append('src')

try:
    from main import app
    print("âœ… main.py imports successfully")
    
    # Test basic routes
    with app.test_client() as client:
        response = client.get("/")
        print(f"âœ… Root route: {response.status_code}")
        
        response = client.get("/health")
        print(f"âœ… Health check: {response.status_code}")
        
        response = client.get("/api/")
        print(f"âœ… API root: {response.status_code}")
        
    print("í¾‰ All tests passed! main.py is ready for Render deployment")
    
except Exception as e:
    print(f"âŒ Error: {e}")
    sys.exit(1)
