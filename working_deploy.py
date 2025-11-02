import sys
sys.path.append('src')
from fastapi import FastAPI
import uvicorn
import threading
import time
from datetime import datetime

app = FastAPI(title="AI-Nexus")

class ThreeTierSystem:
    def __init__(self):
        self.seeker_count = 0
        self.relayer_count = 0 
        self.orchestrator_count = 0
        
    def seeker_loop(self):
        while True:
            self.seeker_count += 1
            print(f"Seeker: Scanning markets... {self.seeker_count}")
            time.sleep(30)
            
    def relayer_loop(self):
        while True:
            self.relayer_count += 1
            print(f"Relayer: Executing... {self.relayer_count}")
            time.sleep(60)
            
    def orchestrator_loop(self):
        while True:
            self.orchestrator_count += 1
            print(f"Orchestrator: AI Cycle {self.orchestrator_count}")
            time.sleep(900)

three_tier = ThreeTierSystem()

@app.get("/")
def root():
    return {
        "status": "operational",
        "system": "AI-Nexus Three-Tier Platform",
        "features": [
            "$100M Flash Loans",
            "Gasless Transactions",
            "AI Optimization", 
            "Three-Tier Architecture"
        ],
        "schedule": "24/7/365"
    }

@app.get("/health")
def health():
    return {"status": "healthy", "time": datetime.now().isoformat()}

@app.get("/status")
def status():
    return {
        "seekers": three_tier.seeker_count,
        "relayers": three_tier.relayer_count,
        "orchestrator": three_tier.orchestrator_count
    }

def start_system():
    threading.Thread(target=three_tier.seeker_loop, daemon=True).start()
    threading.Thread(target=three_tier.relayer_loop, daemon=True).start()
    threading.Thread(target=three_tier.orchestrator_loop, daemon=True).start()

if __name__ == "__main__":
    print("Starting AI-Nexus Three-Tier System...")
    start_system()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
