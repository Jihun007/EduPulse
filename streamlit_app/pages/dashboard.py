import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import platform
from common import move_to, assets_get_img, data_get_csv

if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'

plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 페이지 이동 함수 지정
def fn_goPage(page):
    st.switch_page(page+'.py')

# 버튼 토글
def toggle_info():
    st.session_state['show_info'] = not st.session_state['show_info']

@st.cache_data
# csv 읽어오기
def get_csv():
    file_path = data_get_csv('lowdata.csv')
    csv_file = pd.read_excel(file_path, engine='openpyxl')
    return csv_file

# 대시보드 실행
def run():
    
    # 1. csv 파일 불러오기
    csv_file = get_csv()
    
    title1, title2 = st.columns([6, 1])

    with title1:
        st.image(assets_get_img('logo.png'), width=700)
    with title2:
        # 만족도조사 참여하기 버튼
        if st.button('만족도조사 참여하기', key='surveyBtn1'):
            move_to('survey_form')

    # 줄바꿈
    st.markdown("<br /><br />", unsafe_allow_html=True)

    # 플랫폼 한 줄 소개
    # st.markdown('**EduPusle Dashboard**는 디지털 교육 격차의 실태를 한눈에 보여주고, 정책 수립에 필요한 인사이트를 제공하는 데이터 기반 시각화 플랫폼입니다.')

    # 배너
    st.image(assets_get_img('banner.png'))

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
    #if st.button('EduPulse란?', type="secondary", key='eduPulseBtn'):
    #   toggle_info()

    # show_info 상태가 False 일 경우 소개글 보임
    if st.session_state.get('show_info', False): 
        st.info(text)

    # 줄바꿈
    st.markdown("<br /><br /><br />", unsafe_allow_html=True)
    
    # 탭
    tab = st.tabs(['EduPulse란?'])

    with tab[0]:
        st.image(assets_get_img('tab.png'))
        

    # 전체 필터 구역
    #st.markdown('#### 전체 필터')
    #st.text('원하는 필터를 선택해주세요.')

    highestEdu = ['초등졸 이하', '중졸(고등학교 중퇴 포함)', '고졸(대학교 중퇴 포함)', '대졸(전문대 포함) 이상']
    age = ['10대', '20대', '30대', '40대', '50대', '60대 후반']
    averageMonIncome = ['100만원 미만', '100~199만원', '200~299만원', '300~399만원', '400~499만원', '500~599만원', '600~699만원', '700~799만원', '800~899만원', '900~999만원', '1000만원 이상']

    # 각 필터 3등분하기
    col1, col2, col3 = st.columns(3)

    #with col1:
        #highestEduSelectBox = st.selectbox('**최종학력** : ', highestEdu)
        #highestEduBtn = st.button('**최종학력**', key='filter1')
        
    #with col2:
        #ageSelectBox = st.selectbox('**연령대** : ', age)
        #ageBtn = st.button('**연령대**', key='filter2')

    #with col3:
        #averageMonIncomeSelectBox = st.selectbox('**월평균 소득** : ', averageMonIncome)
        #averageMonIncomeBtn = st.button('**월평균 소득**', key='filter3')

    # 줄바꿈
    st.markdown("<br /><br /><br />", unsafe_allow_html=True)

    #디지털 격차 한 눈에 보기
    #st.markdown('#### 디지털 격차 한 눈에 보기')
    #st.text('지도는 각 시도별 온라인 수업 접근성 점수를 시각화한 것으로, 점수는 응답자의 디지털 기기 활용 경험, 인터넷 접속 가능 여부 등을 기반으로 선정되었습니다.')
    # 임시 사각형 공간
    #st.markdown(
    #    """
    #    <div style="
    #        border: 1px dashed gray;
    #        height: 500px;
    #        width: 100%;
    #        border-radius: 8px;
    #        display: flex;
    #        align-items: center;
    #        justify-content: center;
    #        color: gray;
    #        font-style: italic;
    #    ">
    #        (여기에 그래프가 표시될 예정입니다)
    #    </div>
    #    """,
    #   unsafe_allow_html=True
    #)

    # 각 차트 2구역 나누기
    chart1, chart2 = st.columns(2)
    
    with chart1:
        st.markdown('#### 가구 내 인터넷 가능 여부')
        st.text('막대그래프를 통해 가구 내 인터넷 가능 여부를 확인할 수 있습니다.')

        if csv_file is not None:
            # 2. 엑셀 파일 읽기
            df = csv_file
            df = df.iloc[:, [7, 15]]  # H열(인터넷이용), M열(학력)
            df.columns = ['인터넷이용', '학력']
            
            # 3. 유효 응답 필터링
            df = df[df['인터넷이용'].isin([1, 2]) & df['학력'].isin([1, 2, 3, 4])]

            # 4. 비율 계산
            pivot = pd.crosstab(df['학력'], df['인터넷이용'], normalize='index') * 100

            # 5. 컬럼명, 인덱스 라벨 지정
            rename_map = {}
            if 1 in pivot.columns:
                rename_map[1] = '이용가능'
            if 2 in pivot.columns:
                rename_map[2] = '이용불가능'
            pivot.rename(columns=rename_map, inplace=True)
            pivot.index = ['초등 이하', '중졸', '고졸', '대졸']

            # 6. 시각화
            fig, ax = plt.subplots(figsize=(10, 6))
            pivot.plot(kind='barh', stacked=True, ax=ax, color=['skyblue', 'salmon'])

            # 7. 막대 안에 퍼센트 텍스트 표시
            for i, (idx, row) in enumerate(pivot.iterrows()):
                x_pos = 0
                for val in row:
                    ax.text(x_pos + val / 2, i, f'{val:.1f}%', va='center', ha='center', fontsize=10)
                    x_pos += val

            # 8. 스타일링
            #ax.set_title('학력별 인터넷 이용 가능 여부 (%)')
            #ax.set_xlabel('비율 (%)')
            #ax.set_ylabel('학력 수준')
            ax.set_xlim(0, 100)
            ax.legend(title='인터넷 이용 여부', loc='upper left')
            st.pyplot(fig)
        else:
            st.info("잠시 후 다시 접속해주세요.")

    with chart2:
        st.markdown('#### 디지털 기기 미보유 비율')
        st.text('막대그래프를 통해 디지털 기기 미보유 비율을 확인할 수 있습니다.')

        if csv_file is not None:
            # 파일 읽기 (CSV 또는 XLSX 자동 감지)
            df = csv_file

            # 필요한 열 추출
            try:
                df = df.iloc[:, [2, 3, 4, 5, 15]]
                df.columns = ['데스크탑', '노트북', '휴대전화', '스마트패드', '학력']
            except Exception as e:
                st.error(f"열 인덱스를 읽는 중 오류 발생: {e}")
                st.stop()

            # 디지털 기기 보유 여부 판단
            def check_device_ownership(row):
                return '보유' if (
                    row['데스크탑'] == 1 or
                    row['노트북'] == 1 or
                    row['휴대전화'] == 1 or
                    row['스마트패드'] == 1
                ) else '미보유'

            df['보유여부'] = df.apply(check_device_ownership, axis=1)

            # 🎓 학력 코드 → 라벨 변환
            edu_map = {1: '초등 이하', 2: '중졸', 3: '고졸', 4: '대졸'}
            df['학력'] = df['학력'].map(edu_map)

            # 학력별 보유/미보유 비율 계산
            pivot = pd.crosstab(df['학력'], df['보유여부'], normalize='index') * 100
            if '보유' not in pivot.columns:
                pivot['보유'] = 0
            if '미보유' not in pivot.columns:
                pivot['미보유'] = 0
            pivot = pivot[['보유', '미보유']]  # 보유 → 왼쪽, 미보유 → 오른쪽
            
            order = ['초등 이하', '중졸', '고졸', '대졸']
            pivot = pivot.reindex(order)

            # 시각화
            fig, ax = plt.subplots(figsize=(10, 6))
            pivot.plot(kind='barh', stacked=True, ax=ax, color=['#66b3ff', '#ff9999'])

            # 막대 안 퍼센트 텍스트 표시
            for i, (idx, row) in enumerate(pivot.iterrows()):
                x_pos = 0
                for val in row:
                    ax.text(x_pos + val / 2, i, f'{val:.1f}%', va='center', ha='center', fontsize=10)
                    x_pos += val

            #ax.set_title('학력별 디지털 기기 보유 여부 (%)')
            #ax.set_xlabel('비율 (%)')
            #ax.set_ylabel('학력 수준')
            ax.set_xlim(0, 100)
            ax.legend(title='보유 여부', loc='upper left')
            plt.tight_layout()

            # Streamlit에 출력
            st.pyplot(fig)

        else:
            st.info("잠시 후 다시 접속해주세요.")

    # 줄바꿈
    st.markdown("<br /><br /><br />", unsafe_allow_html=True)

    width1, width2, width3 = st.columns([1, 8, 1])

    with width1:
        ''
    with width2:
        #온라인 수업 플랫폼/기술 사용 경험
        st.markdown('#### 온라인 수업 플랫폼/기술 사용 경험')
        #st.text('자세히 보고싶은 사용 경험을 클릭해주세요.')

        if csv_file is not None:
            # 2. 데이터 불러오기 및 전처리
            df = csv_file
            df = df.iloc[:, [9, 12]]
            df.columns = ['원격회의경험', '학력']
            
            # 3. 유효값 필터링
            df = df[df['원격회의경험'].isin([1, 2, 3, 4]) & df['학력'].isin([1, 2, 3, 4])]

            # 4. 매핑
            exp_map = {
                1: '전혀 그렇지 않다',
                2: '그렇지 않은 편이다',
                3: '그런 편이다',
                4: '매우 그렇다'
            }
            edu_map = {
                1: '초등 이하',
                2: '중졸',
                3: '고졸',
                4: '대졸'
            }
            df['원격회의경험'] = df['원격회의경험'].map(exp_map)
            df['학력'] = df['학력'].map(edu_map)

            # 5. 시각화 (matplotlib → st.pyplot)
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            axes = axes.flatten()

            for i, edu in enumerate(edu_map.values()):
                subset = df[df['학력'] == edu]['원격회의경험'].value_counts().reindex(exp_map.values(), fill_value=0)
                total = subset.sum()
                labels = [f'{label} ({subset[label]/total*100:.1f}%)' for label in subset.index]

                axes[i].pie(
                    subset,
                    labels=labels,
                    autopct='%1.1f%%',
                    startangle=90,
                    counterclock=False,
                    colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']
                )
                axes[i].set_title(f'<{edu} 응답 분포>')

           # plt.suptitle('최종학력별 온라인 수업 플랫폼/기술 사용 경험', fontsize=16)
            plt.tight_layout(rect=[0, 0, 1, 0.96])
            
            # 6. Streamlit에 출력
            st.pyplot(fig)
        else:
            st.info("잠시 후 다시 접속해주세요.")
    with width3:
        ''

    # 줄바꿈
    st.markdown("<br /><br /><br />", unsafe_allow_html=True)

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
    survey1, survey2, survey3 = st.columns([2, 1, 2])
    with survey2:
        # 만족도조사 참여하기 버튼
        if st.button('만족도조사 참여하기', key='surveyBtn2'):
            move_to('survey_form')

if __name__=="__main__":
    run()