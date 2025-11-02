#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import sys

def verify_deployment():
    print("Ì¥ç Verifying AI-Nexus Simulation Deployment...")
    
    # Wait for deployment to be ready
    time.sleep(10)
    
    try:
        # Test health endpoint
        response = requests.get("https://ai-nexus-simulation.onrender.com/health", timeout=30)
        if response.status_code == 200:
            print("‚úÖ Health check: PASSED")
            print(f"   Response: {response.json()}")
        else:
            print("‚ùå Health check: FAILED")
            return False
            
        # Test metrics endpoint
        response = requests.get("https://ai-nexus-simulation.onrender.com/api/metrics", timeout=30)
        if response.status_code == 200:
            print("‚úÖ Metrics endpoint: PASSED")
            metrics = response.json()
            print(f"   Virtual Capital: ${metrics.get('virtual_capital', 0):,}")
            print(f"   Total Profit: ${metrics.get('total_profit', 0):,.2f}")
        else:
            print("‚ùå Metrics endpoint: FAILED")
            return False
            
        # Test dashboard
        response = requests.get("https://ai-nexus-simulation.onrender.com/dashboard", timeout=30)
        if response.status_code == 200:
            print("‚úÖ Dashboard: PASSED")
        else:
            print("‚ùå Dashboard: FAILED")
            return False
            
        print("Ìæâ ALL CHECKS PASSED - AI-Nexus Simulation is LIVE!")
        print("Ìºê Dashboard URL: https://ai-nexus-simulation.onrender.com/dashboard")
        print("Ì≥ä API Base URL: https://ai-nexus-simulation.onrender.com")
        return True
        
    except Exception as e:
        print(f"‚ùå Deployment verification failed: {e}")
        return False

if __name__ == "__main__":
    success = verify_deployment()
    sys.exit(0 if success else 1)
