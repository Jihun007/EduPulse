# requirements.ps1

인코딩 변경
$OutputEncoding = [System.Text.Encoding]::UTF8

1) Python 설치 및 버전 체크
$pythonVersion = python --version 2>&1
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
} else {
    Write-Host "Python 버전 확인에 실패했습니다." -ForegroundColor Yellow
}

Write-Host "Python 버전 확인 성공! 현재 버전: $pythonVersion" -ForegroundColor Green

2) 가상환경 생성 (.venv 폴더)
python -m venv .venv

3) 가상환경 활성화
..venv\Scripts\Activate.ps1

4) pip 업그레이드
python -m pip install --upgrade pip

5) 필수 패키지 설치
pip install streamlit==1.47.0
pip install jupyter==7.3.2
pip install sqlite-bro==0.14.1
pip install matplotlib==3.10.0
pip install openpyxl==3.1.0
pip install numpy==2.2.6

Write-Host ""
Write-Host "가상환경 설정 및 패키지 설치가 완료되었습니다." -ForegroundColor Green

6) Sqlite 및 DB 설치
if (-not (Get-Command -Name "sqlite3" -ErrorAction SilentlyContinue)) {
    Write-Host "sqlite3 명령어가 시스템 PATH에 없습니다. sqlite 실행을 진행합니다."
    # 파이썬 설치코드
    return
}

$ddlFilePath = ".\db\EduPulse_ddl.sql"
$dbFilePath = ".\db\edupulse.db"

sqlite3.exe를 실행하여 DDL 파일 읽기 및 DB 생성
sqlite3 $dbFilePath ".read '$ddlFilePath'"

Write-Host "데이터베이스 생성이 완료되었습니다." -ForegroundColor Green
