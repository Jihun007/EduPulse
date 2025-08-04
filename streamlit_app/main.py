import streamlit as st
from pages import survey_form as form
from pages import survey_result as result
from pages import dashboard as dash


def main():
    st.set_page_config(initial_sidebar_state="collapsed")
    
    page = st.query_params.get("page", [""])[0]
    
    if page == "":
        dash.show()
    # elif page == "survey_form":
    #     form.survey()
    # elif page == "survey_result":
    #     result.result()
    # else:
    #     st.write("존재하지 않는 페이지입니다.")
    
if __name__ == "__main__" :
    main()