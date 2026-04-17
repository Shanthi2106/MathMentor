# Run the Math Mentor API. Always uses this script's folder as project root (PYTHONPATH + .env).
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root
$env:PYTHONPATH = $Root
$Port = 8002
Write-Host "PYTHONPATH=$Root"
Write-Host "API: http://127.0.0.1:${Port}/docs  health: http://127.0.0.1:${Port}/api/health"
Write-Host "If something else already uses this port, change `$Port in run-backend.ps1 and vite.config.js."
# Include .env in reload so key changes apply without editing a .py file (--reload only watches *.py by default).
py -3.13 -m uvicorn backend.main:app --reload --reload-include ".env" --host 127.0.0.1 --port $Port
