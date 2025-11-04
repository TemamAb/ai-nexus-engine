#!/bin/bash

echo "Ì¥ç VERIFYING $250K DAILY PROFIT CONFIGURATION"
echo "=============================================="

# Check all critical files for $250K target
files_to_check=(
    "dashboard/src/components/DashboardHeader.jsx"
    "dashboard/src/components/LiveMetrics.jsx" 
    "dashboard/src/hooks/useProfitMetrics.jsx"
    "src/api/dashboard_controller.py"
    "src/main.py"
    "deploy-dashboard.sh"
)

all_correct=true

for file in "${files_to_check[@]}"; do
    if [ -f "$file" ]; then
        echo ""
        echo "Ì≥Ñ Checking: $file"
        if grep -q "250000\|250000" "$file"; then
            echo "   ‚úÖ $250K target found"
        else
            echo "   ‚ùå $250K target MISSING"
            all_correct=false
        fi
        
        # Check for any incorrect values
        if grep -q "50000\|50000" "$file"; then
            echo "   ‚ö†Ô∏è  Found $50K reference - should be $250K"
            all_correct=false
        fi
    else
        echo "   ‚ùå File not found: $file"
        all_correct=false
    fi
done

echo ""
if [ "$all_correct" = true ]; then
    echo "Ìæâ ALL CONFIGURATIONS CORRECT - $250K DAILY PROFIT TARGET CONFIRMED!"
    echo "Ì∫Ä System ready for deployment"
else
    echo "‚ùå CONFIGURATION ISSUES FOUND - Please fix above errors"
    exit 1
fi

echo ""
echo "Ì≤∞ FINAL CONFIGURATION:"
echo "   ‚Ä¢ Capacity: $100,000,000"
echo "   ‚Ä¢ Daily Target: $250,000" 
echo "   ‚Ä¢ Required ROI: 0.25%"
echo "   ‚Ä¢ Trades Needed: 15-20 high-quality executions"
