import requests
import time
import sys

def check_deployment():
    print("Ì¥ç CHECKING AI-NEXUS DEPLOYMENT STATUS...")
    
    endpoints = [
        ("https://ai-nexus-engine.onrender.com", "Root"),
        ("https://ai-nexus-engine.onrender.com/dashboard", "Dashboard"),
        ("https://ai-nexus-engine.onrender.com/api/institutional/dashboard", "Institutional API"),
        ("https://ai-nexus-engine.onrender.com/api/metrics/live", "Live Metrics"),
        ("https://ai-nexus-engine.onrender.com/api/risk/metrics", "Risk Dashboard")
    ]
    
    all_success = True
    
    for url, name in endpoints:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"‚úÖ {name}: ONLINE (200)")
            else:
                print(f"‚ö†Ô∏è  {name}: RESPONSE {response.status_code}")
                all_success = False
        except requests.exceptions.RequestException as e:
            print(f"‚ùå {name}: OFFLINE - {e}")
            all_success = False
        time.sleep(1)
    
    return all_success

if __name__ == "__main__":
    print("Ì∫Ä AI-NEXUS DEPLOYMENT MONITOR")
    print("==============================")
    
    success = check_deployment()
    
    if success:
        print("\nÌæØ DEPLOYMENT SUCCESSFUL!")
        print("Ì≤∞ AI-Nexus Institutional Dashboard is LIVE")
        print("Ìºê Access your dashboard at: https://ai-nexus-engine.onrender.com/dashboard")
    else:
        print("\n‚è≥ Deployment in progress or partial success...")
        print("   Some endpoints may still be initializing")
        print("   Check Render dashboard for build status")
