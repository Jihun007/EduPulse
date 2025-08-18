# EduPulse

온라인 수업 접근성과 만족도 분석 프로젝트 (2025 오픈소스SW 개발자대회)

# 프로젝트 개요

비대면 수업 환경에서의 접근성과 만족도 간의 관계를 분석하여 공평한 교육 기회 제공 방안을 모색하는 데이터 분석 기반 오픈소스 프로젝트입니다.

# 주요 기능

- 공공데이터 수집 및 전처리
- 온라인 수업 만족도 시각화 대시보드
- 교육 접근성에 따른 격차 분석

# 사용 기술

## <언어 & 개발 환경>
- Python 3.10.11
- Jupyter Notebook 7.3.2
- Streamlit 1.47.0
- Visual Studio Code 1.101.2
- Window 11 (64-bit)

## <가상환경>
- venv
- anaconda 25.5.1

## <주요 라이브러리>
- pandas 2.2.3
- matplotlib 3.10.0
- numpy 2.2.6
- openpyxl 3.0.9

## <데이터베이스>
- SQLite 0.14.1

## <협업 & 버전 관리>
- Git & GitHub
- Google Drive
- Notion

# 프로젝트 구조
```
EduPulse/
├── data/                           # 원본 데이터 및 가공 데이터
│   ├── raw/                        # 수집된 원본 CSV
│   ├── processed/                  # 전처리 완료된 CSV 또는 파생 데이터
│   └── survey/                     # 만족도조사 데이터
│       └── raw/                    # csv
│
├── notebooks/                      # EDA 및 모델링 노트북
│
├── streamlit_app/                  # Streamlit 기반 대시보드 및 설문 시스템
│
├── assets/                         # 이미지 파일
│
├── db/                             # SQLite 파일 위치
│
├── requirements.txt                # 의존성 라이브러리 명시
├── requirements.ps1                # 자동 가상환경 생성 및 패키지 설치
├── README.env.md                   # 프로젝트 설치 및 실행 방법 (간편 실행)
├── README.md                       # 프로젝트 설명 및 실행 방법 (코드 분석)
└── .gitignore                      # Git 제외 파일 설정
```
# 실행 방법

이 프로젝트는 **Python + Jupyter + Pandas + Matplotlib** 기반입니다.
#### 간편 실행만 원하는 경우, `README.env.md`를 참고하세요.

1. Visual Studio Code 설치 (1.101.2)
- https://code.visualstudio.com/

2. Python 설치 (3.10.11)
- https://www.python.org/

3. GitHub clone
- clone 전에 Git 설치(2.50.0.2)
```
# Git Bash에서
git clone https://github.com/Jihun007/EduPulse.git
cd EduPulse
```

4. 가상환경 생성 (권장)
```
# Git Bash에서
# venv 사용 시
python -m venv venv
source venv/Scripts/activate         # Windows
```
5. 필수 패키지 설치
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
6. Jupyter Notebook 사용 (데이터 탐색/분석 단계)
```
pip install jupyter
cd notebooks/
jupyter notebook
```
7. Streamlit 대시보드 실행 (결과 시각화)
```
cd streamlit_app/
streamlit run app.py
```

# 주요 화면 예시
![image](./assets/screen.gif)

# License
본 프로젝트는 MIT License 하에 공개됩니다. 자세한 내용은 `LICENSE` 파일을 참고해주세요.
