import streamlit as st
import json

def getquestion():
    questions = [
        {
            "id": "1",
            "text":"기초 정보",
            "type":"none",
        },
        {
            "id": "1-1",
            "text": "연령",
            "type": "radio",
            "options": [
                "10대", "20대", "30대", "40대", "50대 이상"
            ]
        },
        {
            "id": "1-2",
            "text": "지역",
            "type": "selectbox",
            "options": [
                "서울", "부산", "대전", "인천", "대구", "광주", "울산", "세종", 
                "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"
            ]
        },
        {
            "id": "1-3",
            "text": "최종 학력",
            "type": "radio",
            "options": [
                 "중학교 졸업 이하", "고등학교 졸업", "전문대학(2~3년제) 졸업",
                 "대학교(4년제) 졸업", "대학원 졸업 이상", "기타"
            ]
        },
        {
            "id": "1-4",
            "text": "가구 월평균 소득",
            "type": "radio",
            "options": [   
                "100만 원 미만",                "100만 원 이상 ~ 200만 원 미만", "200만 원 이상 ~ 300만 원 미만",
                "300만 원 이상 ~ 400만 원 미만", "400만 원 이상 ~ 500만 원 미만", "500만 원 이상 ~ 600만 원 미만",
                "600만 원 이상 ~ 700만 원 미만", "700만 원 이상 ~ 800만 원 미만", "800만 원 이상 ~ 900만 원 미만",
                "900만 원 이상 ~ 1000만 원 미만", "1000만 원 이상","응답 거절 / 모르겠음"
            ]
        },
        {
            "id": "2",
            "text": "디지털 기기 보유 여부",
            "type": "none",
        },
        {
            "id": "2-1",
            "text": "디지털 기기 보유 여부",
            "type": "radio",
            "options": [
                "예", "아니오"
            ],
        },
        {
            "id": "2-2",
            "text": "다음 중 내가 원격수업할 때 사용할 수 있는 기기를 모두 선택해 주세요.",
            "type": "checkbox",
            "options": [
                "데스크탑 PC(컴퓨터)", "노트북(컴퓨터)", "휴대폰", "태블릿 PC", "프린터", "웹캠", "기타"
            ],
            "has_etc": True,
            "etc_q":"기타 기기를 입력하세요"
        },
        {
            "id": "2-3",
            "text": "원격수업을 할 때, 주로 어떤 장소에서 원격수업에 참여하셨습니까?",
            "type": "checkbox",
            "options": [
                "내 방에서", "가족과 함께 쓰는 공용 공간에서(예: 거실)", "카페, PC방 등 집 밖에서", "학교 교실에서", "기타"
            ],
            "has_etc": True,
            "etc_q":"기타 징소를 입력하세요"
        },
        {
            "id": "4",
            "text":"지난 학기 또는 최근 몇 차례의 온라인 수업 경험을 기준으로 대답하세요.",
            "type":"none",
        },
        {
            "id": "3-1",
            "text": "온라인 학습을 통해 새로운 지식을 충분히 습득할 수 있었다.",
            "type": "radio",
            "options": [
                 "1. 전혀 그렇지 않다", "2. 그렇지 않다", "3. 보통이다", "4. 그렇다", "5. 매우 그렇다"
            ],
        },
        {
            "id": "3-2",
            "text": "온라인 학습이 문제 해결 능력 향상에 도움이 되었다.",
            "type": "radio",
            "options": [
                 "1. 전혀 그렇지 않다", "2. 그렇지 않다", "3. 보통이다", "4. 그렇다", "5. 매우 그렇다"
            ],
        },
        {
            "id": "3-3",
            "text": "온라인 수업을 통해 수업 목표를 대체로 달성할 수 있었다.",
            "type": "radio",
            "options": [
                 "1. 전혀 그렇지 않다", "2. 그렇지 않다", "3. 보통이다", "4. 그렇다", "5. 매우 그렇다"
            ],
        },
        {
            "id": "4",
            "text":"당신이 그동안 참여한 온라인 수업 전반에 대한 인식을 묻습니다.",
            "type":"none",
        },
        {
            "id": "4-1",
            "text": "전반적으로 온라인 학습에 만족한다.",
            "type": "radio",
            "options": [
                 "1. 전혀 그렇지 않다", "2. 그렇지 않다", "3. 보통이다", "4. 그렇다", "5. 매우 그렇다"
            ],
        },
        {
            "id": "4-2",
            "text": "온라인 학습 경험이 기대 이상이었다.",
            "type": "radio",
            "options": [
                 "1. 전혀 그렇지 않다", "2. 그렇지 않다", "3. 보통이다", "4. 그렇다", "5. 매우 그렇다"
            ],
        },
        {
            "id": "4-3",
            "text": "같은 조건이라면 다음에도 온라인 수업 방식을 선택할 것이다",
            "type": "radio",
            "options": [
                 "1. 전혀 그렇지 않다", "2. 그렇지 않다", "3. 보통이다", "4. 그렇다", "5. 매우 그렇다"
            ],
        },
    ]
    return questions

def survey():
    
    st.markdown("""
        <style>
        /* 1. 라디오 버튼 그룹의 컨테이너 설정 */
        div.stRadio > label {
            flex-direction: row; /* 라벨과 라디오 버튼을 가로로 정렬 (큰 의미 없음) */
            align-items: flex-start; /* 라디오 그룹 전체를 상단 정렬 (기본) */
        }

        /* 2. 실제 라디오 옵션들이 들어있는 컨테이너 (role="radiogroup") */
        div.stRadio div[role="radiogroup"] {
            display: flex; /* Flexbox 레이아웃 사용 */
            flex-wrap: wrap; /* 공간 부족 시 다음 줄로 넘김 */
            gap: 15px 20px; /* 세로 간격 15px, 가로 간격 20px (조정 가능) */
            /* justify-content: flex-start; */ /* 왼쪽 정렬 (기본) */
            /* justify-content: center; */ /* 가운데 정렬 (필요시) */
        }

        /* 3. 각 개별 라디오 옵션 (버튼 원 + 텍스트)의 스타일 */
        div.stRadio div[data-baseweb="radio"] {
            /* flex-basis: calc(33.33% - 20px); */ /* 3개씩 한 줄에 배치 (가로 간격 고려) */
            /* flex-basis는 컨텐츠의 기본 크기를 지정합니다. */
            width: calc(33.33% - 20px); /* 3개씩 한 줄에 배치 (가로 간격 고려) */
            /* width를 직접 지정하는 것이 더 예측 가능할 때가 있습니다. */
            min-width: 150px; /* 최소 너비 (텍스트가 잘리지 않도록) */
            margin-right: 0px; /* 기본 마진 제거 */
            margin-bottom: 0px; /* 기본 마진 제거 */
            box-sizing: border-box; /* 패딩과 보더가 width에 포함되도록 */
        }

        /* 4. 라디오 버튼 원과 텍스트를 감싸는 내부 라벨 (가로 정렬, 세로 중앙 정렬) */
        div.stRadio label > div:first-child { /* 라디오 원을 감싸는 div */
            align-self: center; /* 라디오 원을 텍스트의 세로 중앙에 맞춤 */
        }
        div.stRadio span[data-testid="stRadioInlineLabel"] {
            margin-left: 5px; /* 라디오 원과 텍스트 사이 간격 */
            flex-grow: 1; /* 텍스트가 남은 공간을 채우도록 */
            display: flex; /* 텍스트 자체도 Flexbox로 (필요시) */
            align-items: center; /* 텍스트 내부 정렬 (필요시) */
            min-height: 2em; /* 텍스트가 여러 줄일 때 대비 (선택 사항) */
        }

        /* 5. Streamlit의 기본 라디오 버튼 라벨 (질문 텍스트)이 있다면, 이 CSS는 그 라벨의 레이아웃을 건드리지 않도록 합니다. */
        /* 만약 st.radio의 첫 번째 인자로 질문 텍스트를 넣었다면, 그 텍스트 스타일링은 별도로 고려해야 합니다. */
        </style>
        """, unsafe_allow_html=True)
    

    st.header("온라인 학습 환경과 경험에 대한 실태조사")

    with st.container():
        st.markdown(
            """
            <div style="background-color:#F0F0F0;padding:16px;border-radius:8px;">
            안녕하세요.<br><br>
            EduPulse에서는 원격수업 및 디지털 학습 환경에서 나타나는 학습 경험의 차이를 이해하고, 교육 격차 해소를 위한 <b>데이터 기반 정책 수립</b>을 위해 이 설문을 진행하고 있습니다.<br><br>
            본 조사는 디지털 환경 접속, 수업 참여도, 학습 동기 및 만족도 등 다양한 요소를 바탕으로 학습 경험의 특성을 분석하기 위한 것입니다.<br>
            응답해주신 내용은 모두 익명으로 처리되며, 통계 분석 및 교육 정책 개선 이외의 목적으로는 사용되지 않습니다.<br>
            바쁘시겠지만 정성껏 응답해주시면 미래 교육환경 개선에 큰 도움이 됩니다.<br><br>
            <b>ㆍ조사대상:</b> 원격수업 또는 디지털 수업에 참여한 경험이 있는 모든 학습자<br>
            <b>ㆍ참여시간:</b> 약 5분 (총 13문항)<br>
            <b>ㆍ조사기간:</b> 상시<br>
            <b>ㆍ주관:</b> EduPulse
            </div>
            """, unsafe_allow_html=True
        )

    st.write(" ")

    questions = getquestion()

    responses = {}
    etc_dict = {}

    # form 밖에서 문항 UI 렌더링
    for q in questions:
        qid = q["id"]
        qtext = q["text"]
        qtype = q["type"]
        qtitle = qid + ". " + qtext
        qoptions = q.get("options", [])
        
        option_to_num = {opt: i+1 for i, opt in enumerate(qoptions)}  

        if qtype == "radio":
            
            st.markdown(f"<p style='font-size:16px; font-weight:bold;'>{qtitle}</p>", unsafe_allow_html=True)
            answer = st.radio("", options=qoptions, key=qid, horizontal=True, index=None)
            res = option_to_num.get(answer)
            responses[qid] = res
            
            if q.get("has_etc") and answer == "기타":
                etc_input = st.text_input(q.get("etc_q", "기타 내용을 입력하세요"), key=f"{qid}_etc")
                etc_dict[qid] = etc_input

        elif qtype == "selectbox":
            st.markdown(f"<p style='font-size:16px; font-weight:bold;'>{qtitle}</p>", unsafe_allow_html=True)
            answer = st.selectbox("", options=qoptions, key=qid, index=None)
            res = option_to_num.get(answer)
            responses[qid] = res

            if q.get("has_etc") and selected == "기타":
                etc_input = st.text_input(q.get("etc_q", "기타 내용을 입력하세요"), key=f"{qid}_etc")
                etc_dict[qid] = etc_input

        elif qtype == "checkbox":
            st.write(f"**{qtitle}**")

            selected = []
            cols = st.columns(3)
            for i, option in enumerate(qoptions):
                key = f"{qid}_{i}"
                if cols[i % 3].checkbox(option, key=key):
                    res = option_to_num.get(option)
                    selected.append(res)
            responses[qid] = selected

            # '기타' 선택 시 텍스트 입력창 노출
            if q.get("has_etc") and st.session_state.get(f"{qid}_{qoptions.index('기타')}", False):
                etc_input = st.text_input(q.get("etc_q", "기타 내용을 입력하세요"), key=f"{qid}_etc")
                etc_dict[qid] = etc_input

        elif qtype == "text":
            text_input = st.text_input(f"**{qtitle}**", key=qid)
            responses[qid] = text_input

        elif qtype == "none":
            st.divider()
            st.markdown(f"<p style='font-size:22px; font-weight:bold;'>{qtitle}</p>", unsafe_allow_html=True)
            
        else:
            continue
        
        st.write()
        st.write()

    # 제출 버튼만 form으로 묶기 (submit 용)
    with st.form("submit_form"):
        submitted = st.form_submit_button("제출")

    if submitted:  
        
        # 데이터 검증
        is_valid = True
        error_message = ""
        for q in questions:
            qid = q["id"]
            qtext = q["text"]
            qtype = q["type"]
            
            if qtype == "radio" or qtype == "selectbox":
                if responses.get(qid) is None:
                    is_valid = False
                    error_message = f"🚨 '{qtext}' 문항을 선택해주세요."
                    break
            elif qtype == "checkbox":
                if not responses.get(qid): # 선택된 항목이 없으면
                    is_valid = False
                    error_message = f"🚨 '{qtext}' 문항을 하나 이상 선택해주세요."
                    break
            elif qtype == "text":
                if not responses.get(qid): # 입력된 텍스트가 없으면
                    is_valid = False
                    error_message = f"🚨 '{qtext}' 문항에 내용을 입력해주세요."
                    break
        
            # '기타' 항목의 텍스트 입력 검사
            if q.get("has_etc") and qid in etc_dict and not etc_dict[qid]:
                is_valid = False
                error_message = f"🚨 '{qtext}' 문항의 기타 내용을 입력해주세요."
                break
        
        if is_valid:

            # dictionary 형태로 진행
            final_responses = responses.copy()
            final_responses.update(etc_dict)
            
            st.session_state['form_data'] = final_responses
            
            # 페이지 이동
            st.switch_page("pages/survey_result.py") # 'result.py'로 변경합니다.
        else:
            st.error(error_message)
        

if __name__ == "__main__":
    survey()