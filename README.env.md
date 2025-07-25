# 📝EduPulse
- 온라인 수업 접근성과 만족도 분석 프로젝트의 개발 환경 및 실행 방법 안내

이 문서는 온라인 수업 접근성과 만족도 분석 프로젝트 개발환경을 구성하고 실행하기 위한 가이드를 제공합니다.


## 프로젝트 개요
- 


## 🖥️ 사용한 기술
- OS: Windows 11 이상, macOS, Linux (Windows 11 권장)  
- Python: 3.10.11 이상
- anaconda: 25.5.1 (데이터 분석을 위해 사용)  
- SQLite: 0.14.1
- Streamlit: 1.47.0
- Jupyter notebook: 7.3.2
- 가상환경 권장 (venv 또는 conda 사용 권장)


## 💡 실행 화면
*프로젝트 실행 시 주요 화면 또는 기능 스크린샷을 여기에 추가.*


## ❓ 설치 및 실행 방법

### 1. 저장소 클론 및 프로젝트 폴더 이동
```bash
git clone https://github.com/Jihun007/EduPulse
cd eduPulse
```
### 2. Windows 환경: 자동 가상환경 생성 및 패키지 설치 (권장)
 - Windows PowerShell에서 실행하세요:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\requirements.ps1
```

### 3. macOS / Linux 환경: 수동 설치
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. 프로젝트 실행
```
streamlit run main.py
```
