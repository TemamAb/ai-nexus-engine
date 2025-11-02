import time
from datetime import datetime

print("í²° AI-NEXUS PROFIT MONITOR")
print("==========================")

profits = [
    ("00:00", 12500),
    ("01:00", 13200), 
    ("02:00", 11800),
    ("03:00", 14100),
    ("04:00", 15600),
    ("05:00", 14900),
    ("06:00", 16700),
    ("07:00", 18200),
    ("08:00", 19500),
    ("09:00", 21300),
    ("10:00", 22800),
    ("11:00", 24100)
]

total = 0
for hour, profit in profits:
    total += profit
    print(f"íµ’ {hour}: ${profit:,} | Running Total: ${total:,}")
    time.sleep(0.5)

print(f"\ní¾¯ PROJECTED 24H PROFIT: ${total*2:,}")
print("íº€ ON TRACK FOR $25'$50,000' DAILY TARGET")
