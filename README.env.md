## 사용 기술 요약

- **언어/환경**: Python 3.10.11, Jupyter Notebook, Streamlit
- **가상환경**: venv 또는 conda 권장
- **주요 라이브러리**: pandas, streamlit, matplotlib 등
- **DB**: SQLite (로컬 파일 기반)
- **OS**: Windows 11 기준 개발

## 설치 및 실행 방법

### 1. 저장소 클론 및 프로젝트 폴더 이동
```bash
git clone https://github.com/Jihun007/EduPulse
cd eduPulse
```
### 2. Windows 환경: 자동 가상환경 생성 및 패키지 설치 (권장)
 - Windows PowerShell에서 실행하세요.
 - Python 3.10.11 설치를 먼저 하세요.
```powershell
powershell.exe -ExecutionPolicy Bypass -File ".\requirements.ps1"
```

### 3. macOS / Linux 환경: 수동 설치
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. 프로젝트 실행
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\activate
cd streamlit_app
streamlit run app.py
```
