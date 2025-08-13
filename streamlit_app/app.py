import streamlit as st
from common import init_page, current_page, scroll_to_top
from pages import dashboard, survey_form, survey_result

# 페이지 기본 설정
st.set_page_config(
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 사이드바 및 설정 아이콘 숨기기
hide_streamlit_style = """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="collapsedControl"] {
        display: none;
    }
    [data-testid="stExpandSidebarButton"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 페이지 상태 초기화 (main)
init_page()

# 현재 페이지 반환 함수 : page키가 없을 경우 기본값으로 main 반환
page = current_page()

# 화면 제일 상단으로 이동
#scroll_to_top()

if page == 'main':
    dashboard.run()
elif page == 'survey_form':
    survey_form.survey()
elif page == 'survey_result':
    survey_result.finish()