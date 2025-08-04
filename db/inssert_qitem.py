import os
import sqlite3 as sql
from streamlit_app.pages import survey_form as form

# DB 정보
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DB_FOLDER = os.path.join(PARENT_DIR, "db")
# 데이터베이스 파일 연결 (파일이 없으면 생성됨)
os.makedirs(DB_FOLDER, exist_ok=True)
DB_PATH = os.path.join(DB_FOLDER, "survey.db")

def connect_db():
    return sql.connect(DB_PATH)

def insert_data():
    conn = None
    try:
        
        conn = connect_db()
        cur = conn.cursor()   
        
        data = get_data()
        
        insert_query = f"""
            INSERT INTO QITEM (QITEM_NUM, QITEM_NM) VALUES (?, ?)
        """
        

    except sql.IntegrityError as e:
        return False
    except sql.Error as e:
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()
    
def get_data():
    # 삽입용 데이터
    questions = form.getquestion()
    
    filtered_data = {}
    id_counter = 1;
    for key, value in questions.items():
        filtered_data['id'] = 'Q' + id_counter
        id_counter = + 1;
        if isinstance(value, dict) and 'type' in value and value['type'] == 'none':
            # type이 "none"인 경우 건너뛰기
            continue
        elif isinstance(value, dict) and 'text' in value:
            # 딕셔너리 형태이고 'text' 키가 있는 경우
            filtered_data[key] = value['text']
        else:
            continue

    print(f"필터링된 데이터: {filtered_data}")
    
    return filtered_data
   
        