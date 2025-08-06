import streamlit as st
from common import move_to, assets_get_img

# 페이지 이동 함수 지정
def fn_goPage(page):
    st.switch_page(page+'.py')

# 버튼 토글
def toggle_info():
    st.session_state['show_info'] = not st.session_state['show_info']

def run():
    
    title1, title2 = st.columns([6, 1])

    with title1:
        st.image(assets_get_img('logo.png'))
        # 제목
        st.title('EduPulse Dashboard')
    with title2:
        # 만족도조사 참여하기 버튼
        if st.button('만족도조사 참여하기', key='surveyBtn1'):
            move_to('survey_form')


    # 플랫폼 한 줄 소개
    st.markdown('**EduPusle Dashboard**는 디지털 교육 격차의 실태를 한눈에 보여주고, 정책 수립에 필요한 인사이트를 제공하는 데이터 기반 시각화 플랫폼입니다.')

    # 소개 글
    text = '''
    “온라인 수업은 모두에게 공평하게 제공되었는가?”
    EduPulse는 이 질문에서 출발했습니다.

    본 플랫폼은 디지털 접근성, 지역·계층별 차이, 지역 참여 환경 등을 분석하고 시각화함으로써, 코로나 이후 심화된 교육 격차의 원인을 정량적으로 조명합니다.

    실시간 필터링과 지역별 비교를 통해, 누구나 쉽게 격차의 양상을 확인하고, 정책 설계자와 교육 관계자들이 효과적인 대응책을 수립할 수 있도록 지원합니다.

    EduPulse는 궁극적으로 모두에게 공평한 교육 환경을 실현하는 것을 목표로 합니다.
    '''

    # show_info 선언
    if 'show_info' not in st.session_state:
        st.session_state['show_info'] = False

    # 'EduPulse란?' 버튼 클릭 시 토글 발동
    if st.button('EduPulse란?', type="secondary", key='eduPulseBtn'):
        toggle_info()

    # show_info 상태가 False 일 경우 소개글 보임
    if st.session_state.get('show_info', False): 
        st.info(text)

    # 전체 필터 구역
    st.markdown('#### 전체 필터')
    st.text('원하는 필터를 선택해주세요.')

    highestEdu = ['초등졸 이하', '중졸(고등학교 중퇴 포함)', '고졸(대학교 중퇴 포함)', '대졸(전문대 포함) 이상']
    age = ['10대', '20대', '30대', '40대', '50대', '60대 후반']
    averageMonIncome = ['100만원 미만', '100~199만원', '200~299만원', '300~399만원', '400~499만원', '500~599만원', '600~699만원', '700~799만원', '800~899만원', '900~999만원', '1000만원 이상']

    # 각 필터 3등분하기
    col1, col2, col3 = st.columns(3)

    with col1:
        #highestEduSelectBox = st.selectbox('**최종학력** : ', highestEdu)
        highestEduBtn = st.button('**최종학력**', key='filter1')
        
    with col2:
        #ageSelectBox = st.selectbox('**연령대** : ', age)
        ageBtn = st.button('**연령대**', key='filter2')

    with col3:
        #averageMonIncomeSelectBox = st.selectbox('**월평균 소득** : ', averageMonIncome)
        averageMonIncomeBtn = st.button('**월평균 소득**', key='filter3')

    # 줄바꿈
    st.markdown("<br />", unsafe_allow_html=True)

    #디지털 격차 한 눈에 보기
    st.markdown('#### 디지털 격차 한 눈에 보기')
    st.text('지도는 각 시도별 온라인 수업 접근성 점수를 시각화한 것으로, 점수는 응답자의 디지털 기기 활용 경험, 인터넷 접속 가능 여부 등을 기반으로 선정되었습니다.')
    # 임시 사각형 공간
    st.markdown(
        """
        <div style="
            border: 1px dashed gray;
            height: 500px;
            width: 100%;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: gray;
            font-style: italic;
        ">
            (여기에 그래프가 표시될 예정입니다)
        </div>
        """,
        unsafe_allow_html=True
    )

    # 줄바꿈
    st.markdown("<br />", unsafe_allow_html=True)

    # 각 차트 2구역 나누기
    chart1, chart2 = st.columns(2)

    with chart1:
        st.markdown('#### 가구 내 인터넷 가능 여부')
        st.text('막대그래프를 통해 가구 내 인터넷 가능 여부를 확인할 수 있습니다.')
        # 임시 사각형 공간
        st.markdown(
            """
            <div style="
                border: 1px dashed gray;
                height: 300px;
                width: 100%;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: gray;
                font-style: italic;
            ">
                (여기에 그래프가 표시될 예정입니다)
            </div>
            """,
            unsafe_allow_html=True
        )
    with chart2:
        st.markdown('#### 디지털 기기 미보유 비율')
        st.text('막대그래프를 통해 디지털 기기 미보유 비율을 확인할 수 있습니다.')
        # 임시 사각형 공간
        st.markdown(
            """
            <div style="
                border: 1px dashed gray;
                height: 300px;
                width: 100%;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: gray;
                font-style: italic;
            ">
                (여기에 그래프가 표시될 예정입니다)
            </div>
            """,
            unsafe_allow_html=True
        )

    # 줄바꿈
    st.markdown("<br />", unsafe_allow_html=True)

    #온라인 수업 플랫폼/기술 사용 경험
    st.markdown('#### 온라인 수업 플랫폼/기술 사용 경험')
    st.text('자세히 보고싶은 사용 경험을 클릭해주세요.')
    # 임시 사각형 공간
    st.markdown(
        """
        <div style="
            border: 1px dashed gray;
            height: 300px;
            width: 100%;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: gray;
            font-style: italic;
        ">
            (여기에 그래프가 표시될 예정입니다)
        </div>
        """,
        unsafe_allow_html=True
    )

    # 줄바꿈
    st.markdown("<br />", unsafe_allow_html=True)

    #만족도조사
    st.markdown('#### 만족도조사')
    st.text('EduPulse에서 실행한 만족도조사 결과가 반영되어 있습니다.')
    # 임시 사각형 공간
    st.markdown(
        """
        <div style="
            border: 1px dashed gray;
            height: 300px;
            width: 100%;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: gray;
            font-style: italic;
        ">
            (여기에 그래프가 표시될 예정입니다)
        </div>
        """,
        unsafe_allow_html=True
    )

    # 줄바꿈
    st.markdown("<br />", unsafe_allow_html=True)

    # 버튼 가운데
    survey1, survey2, survey3 = st.columns(3)
    with survey2:
        # 만족도조사 참여하기 버튼
        if st.button('만족도조사 참여하기', key='surveyBtn2'):
            move_to('survey_form')

if __name__=="__main__":
    run()