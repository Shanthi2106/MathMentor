# Run the Math Mentor API (from project root)
# Use Python 3.13 so packages are found (py -3.13 -m pip install -r backend\requirements.txt)
$env:PYTHONPATH = (Get-Location).Path
py -3.13 -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
