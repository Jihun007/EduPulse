import streamlit as st
from pages import survey_form as form
from pages import survey_result as result


def main():
    st.set_page_config(initial_sidebar_state="collapsed")
    
    page = st.query_params.get("page", [""])[0]
    
    # if st.session_state.get("page"):
    #     page = st.session_state["page"]
        
    st.write(page)
    
    if page == "":
        st.write("메인페이지")
        return
    elif page == "survey_form":
        form.survey()
    # elif page == "survey_result":
    #     result.result()
    else:
        st.write("존재하지 않는 페이지입니다.")
    
    # responses = form.survey()

    # if responses:  
    #     if data_handlr.validate(responses):
    #         data_handlr.save(responses)
    #         st.success("저장 완료")
    
if __name__ == "__main__" :
    main()