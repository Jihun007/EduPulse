import os
import sqlite3 as sql
from datetime import datetime

# db - survey.db 경로 설정
# 현재 스크립트 파일의 절대 경로
current_script_path = os.path.abspath(__file__)
# 현재 스크립트의 디렉토리(services)
current_dir = os.path.dirname(current_script_path)
# 2단계 상위 디렉토리(streamlit_app)
parent_dir_upper = os.path.dirname(current_dir)
# 상위 디렉토리(Edupurse) -  '..'는 상위 디렉토리를 의미
parent_dir = os.path.dirname(parent_dir_upper)
# 상위 디렉토리에서 ''data' 폴더로 이동. db 파일 경로 설정
DB_PATH = os.path.join(parent_dir, 'db', 'survey.db')

def connect_db():
    return sql.connect(DB_PATH)

def save(data_list):
    
    print(f"data:{data_list}")
  
    insert_query = f"""
            INSERT INTO DGSTFN (RSPDNT_DATE, 
                                Q1, Q2, Q3, Q4, Q5, 
                                Q6, Q7, Q8, Q9, Q10,
                                Q11, Q12, Q13) 
            VALUES (?, 
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, 
                    ?, ?, ?)
        """
        
    # columns = list(data_list.keys())
    # placeholders = ', '.join(['?'] * len(columns))
    # insert_query = f"INSERT INTO SurveyResponses ({', '.join(columns)}) VALUES ({placeholders});"
    
    processed_values = []
    for value in data_list.values():
        if isinstance(value, list):
            # 리스트일 경우, 리스트 내부의 각 항목을 processed_values에 추가
           processed_values.append(", ".join(map(str, value)))
        else:
            # 리스트가 아닐 경우, 원래 값을 그대로 추가
            processed_values.append(value)
            
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    processed_values.insert(0, current_date)

    values_tuple = tuple(processed_values)
   
    print(f"원본 딕셔너리: {data_list}")
    print(f"처리된 튜플: {values_tuple}")
  
    try:
        
        conn = connect_db()
        cur = conn.cursor()   
        
        cur.execute(insert_query, values_tuple) 
        
        conn.commit()
        print(f"총 {len(data_list)}개의 데이터가 성공적으로 삽입되었습니다.")
        
    except sql.IntegrityError as e: # 중복된 키 등 무결성 제약 조건 위반 시
        print(f"무결성 오류가 발생했습니다 (Primary Key 중복 등): {e}")
        if conn:
            conn.rollback()
    except sql.Error as e: # SQLITE3에서 발생하는 모든 에러 (예: 테이블/컬럼명이 잘못되었거나, VALUES 수가 맞지 않을 때)
        print(f"SQLITE3 오류가 발생했습니다: {e}")
        if conn:
            conn.rollback()
    except Exception as e: # 위 두 가지 외에 발생하는 모든 예상치 못한 에러
        print(f"예상치 못한 오류가 발생했습니다: {e}")
        if conn:
            conn.rollback()
            return False
    finally:
        if conn:
            conn.close()


