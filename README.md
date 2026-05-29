# SD Invoice V5.7.1 Render HEAD & Template Recovery Fix

Fixes:
- Render HEAD / error
- Adds /health and /ready
- Ensures all required templates exist
- Keeps full ERP menu
- Keeps V5.7 document entry format structure

Render:
Build Command: pip install -r requirements.txt
Start Command: gunicorn run:app

Test:
1. /health
2. /
3. /admin
