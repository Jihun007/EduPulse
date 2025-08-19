# 실패 시 즉시 중단
$ErrorActionPreference = 'Stop'

Write-Host "Check Python version..."
python --version

# venv 생성
if (!(Test-Path ".\.venv")) {
    Write-Host "Creating a virtual environment (.venv)..."
    python -m venv .venv
} else {
    Write-Host "Existing .venv detected. Skipp Creating step."
}

# 가상환경 활성화 (PowerShell 전용)
$activate = ".\.venv\Scripts\Activate.ps1"
if (!(Test-Path $activate)) {
    throw "No virtual environment activation script: $activate (check if venv creation failed)"
}
Write-Host "Activating the virtual environment..."
& $activate

# pip 인코딩/경로 안정화
$env:PYTHONUTF8 = "1"

Write-Host "pip upgrade ..."
python -m pip install --upgrade pip

Write-Host "Install requirements..."
python -m pip install -r requirements.txt

Write-Host "Installation complete"

