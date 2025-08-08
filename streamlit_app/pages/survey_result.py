import streamlit as st
from services import data_handlr as handlr
from common import move_to

def survey():
    st.set_page_config(
        page_title="결과",
        page_icon="🎉",
        layout="wide"
    )

    st.write()
    st.write()
    st.write()
    # 페이지 레이아웃 조정 (센터링 효과)
    st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

    # # 제목 (좌측 정렬)
    # st.markdown('<h3 style="font-weight:bold; margin-bottom:0.5em;">만족도조사</h3>', unsafe_allow_html=True)

    # 가운데 내용
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(
        "<h2 style='text-align:center; font-weight:bold;'>만족도 조사가 완료되었습니다.</h2>",
        unsafe_allow_html=True
    )

    # 아이콘/이미지 (로컬 이미지 파일일 경우 경로와 파일명에 맞게 변경)
    # st.image("handshake.png", width=220, use_column_width=False, output_format="auto", caption=None)  # 예) ./handshake.png

    # 안내 문구
    st.markdown(
        """
        <div style='text-align:center; font-size:1.07em; margin-top:2em; margin-bottom:2em;'>
        소중한 시간을 내어 응답해주셔서 진심으로 감사드립니다.<br><br>
        여러분의 의견은 향후 <b>디지털 교육 환경 개선 및 교육 격차 해소를 위한 정책 수립</b>에 소중한 자료로 활용됩니다.<br>
        다시 한 번 귀중한 참여에 감사드립니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    # 메인으로 버튼 (가운데 정렬)
    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        if st.button("메인으로", use_container_width=True):
            move_to('main') #통계화면으로 이동하도록 수정 필요

    # st.session_state에서 form.py에서 저장한 데이터를 가져옵니다.
    if 'form_data' in st.session_state:
        form_data = st.session_state.form_data
        
        # 데이터 처리
        handlr.save(form_data)
        st.subheader("데이터 처리 결과")
        st.success("데이터가 저장되었습니다.")
        
        # 데이터 확인용
        st.json(form_data)
        
        # 세션 상태에서 폼 데이터를 삭제하여 새로고침 시 데이터가 남아있지 않도록 합니다.
        del st.session_state['form_data']
        
    else:
        st.warning("제출된 데이터가 없습니다. 설문조사 페이지로 이동하여 다시 시작해주세요.")
        if st.button("설문조사 페이지로 돌아가기"):
            move_to('main')

if __name__ == "__main__":
    survey()