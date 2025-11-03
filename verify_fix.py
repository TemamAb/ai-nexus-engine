import os
print("Ì¥ç ACTUAL FILE CONTENT VERIFICATION:")
with open('app.py', 'r') as f:
    content = f.read()
    if '$100M' in content and '$250,000' in content:
        print("‚úÖ app.py contains CORRECT: $100M and $250,000")
    else:
        print("‚ùå app.py still has issues")
        print("CONTENT SNIPPET:")
        print(content[:500])
