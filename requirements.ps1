# requirements.ps1

# 인코딩 변경
chcp 65001 > $null    # cmd 창 코드페이지를 UTF-8로
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# 1) Python 설치 및 버전 체크
$pythonVersion = py --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Python이 설치되어 있지 않습니다. https://www.python.org/downloads/ 에서 설치하세요." -ForegroundColor Red
    exit 1
}

$versionMatch = $pythonVersion -match "Python (\d+).(\d+).(\d+)"
if ($versionMatch) {
    $major = [int]$Matches[1]
    $minor = [int]$Matches[2]

    if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 10)) {
        Write-Host "Python 3.10 이상이 필요합니다. 현재 버전: $pythonVersion" -ForegroundColor Red
        Write-Host "https://www.python.org/downloads/ 에서 최신 버전을 설치하세요."
        exit 1
    }

    Write-Host "Python 버전 확인 성공! 현재 버전: $pythonVersion" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "Python 버전 확인에 실패했습니다." -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

Write-Host "가상환경 설치 및 필수 패키지 설치중..."

# 2) pip 업그레이드
Write-Host "pip 업그레이드 중..."
py -m pip install --upgrade pip

# 3) 가상환경 생성 (.venv 폴더)
py -m venv .venv

# 4) 가상환경 활성화 및 필수 패키지 설치
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

Write-Host ""
Write-Host "가상환경 설정 및 패키지 설치가 완료되었습니다." -ForegroundColor Green
