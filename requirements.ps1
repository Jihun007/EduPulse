# 실패 시 즉시 중단
$ErrorActionPreference = 'Stop'

Write-Host "Python 버전 확인..."
python --version

# venv 생성
if (!(Test-Path ".\.venv")) {
    Write-Host "가상환경(.venv) 생성..."
    python -m venv .venv
} else {
    Write-Host "기존 .venv 감지됨. 생성 단계 건너뜀."
}

# 가상환경 활성화 (PowerShell 전용)
$activate = ".\.venv\Scripts\Activate.ps1"
if (!(Test-Path $activate)) {
    throw "가상환경 활성화 스크립트가 없습니다: $activate (venv 생성 실패 여부 확인)"
}
Write-Host "가상환경 활성화..."
& $activate

# pip 인코딩/경로 안정화
$env:PYTHONUTF8 = "1"

Write-Host "pip 업그레이드..."
python -m pip install --upgrade pip

Write-Host "requirements 설치..."
python -m pip install -r requirements.txt

Write-Host "완료"

# 실패 시 즉시 중단
$ErrorActionPreference = 'Stop'

Write-Host "Python 버전 확인..."
python --version

# venv 생성
if (!(Test-Path ".\.venv")) {
    Write-Host "가상환경(.venv) 생성..."
    python -m venv .venv
} else {
    Write-Host "기존 .venv 감지됨. 생성 단계 건너뜀."
}

# 가상환경 활성화 (PowerShell 전용)
$activate = ".\.venv\Scripts\Activate.ps1"
if (!(Test-Path $activate)) {
    throw "no venv activate script: $activate (venv 생성 실패 여부 확인)"
}
Write-Host "venv activate..."
& $activate

# pip 인코딩/경로 안정화
$env:PYTHONUTF8 = "1"

Write-Host "pip upgrade..."
python -m pip install --upgrade pip

Write-Host "requirements install..."
python -m pip install -r requirements.txt

Write-Host "complete"
