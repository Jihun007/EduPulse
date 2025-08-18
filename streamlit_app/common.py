import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 페이지 상태 초기화 (main)
def init_page(default='main'):
    if 'page' not in st.session_state:
        st.session_state['page'] = default

# 다른 페이지로 이동하는 함수
def move_to(page_name: str):
    st.session_state['page'] = page_name
    st.rerun()

# 현재 페이지 반환 함수 : page키가 없을 경우 기본값으로 main 반환
def current_page():
    return st.session_state.get('page', 'main')  

# 화면 제일 상단으로 이동
def scroll_to_top():
    components.html(
        """
        <script>
            window.parent.scrollTo(0, 0);
        </script>
        """,
        height=0,
    )
# 현재 파일 기준으로 이미지 절대 경로 생성   
def assets_get_img(img_name):
    return Path(__file__).parent.parent / 'assets' / img_name

# 현재 파일 기준으로 csv 절대 경로 생성   
def data_get_csv(csv_name):
    return Path(__file__).parent.parent / 'data/processed' / csv_name

# 현재 파일 기준으로 만족도조사 csv 절대 경로 생성
def data_get_surCsv(csv_name):
    return Path(__file__).parent.parent / 'data/survey/raw' / csv_name