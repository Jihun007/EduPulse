import os
import sqlite3

# 1. 절대 경로 기반 DB 파일 경로 설정 및 폴더 생성
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DB_FOLDER = os.path.join(PARENT_DIR, "db")
# 데이터베이스 파일 연결 (파일이 없으면 생성됨)
os.makedirs(DB_FOLDER, exist_ok=True)
DB_PATH = os.path.join(DB_FOLDER, "survey.db")
# DDL 파일 연결
DDL_SQL_FILE = 'EduPulse_ddl.sql'
DDL_SQL_PATH = os.path.join(DB_FOLDER, DDL_SQL_FILE)

# 2. DB 연결 함수
def connect_db():
    return sqlite3.connect(DB_PATH)

# 3. 최초 실행 시 DB와 테이블 생성 함수
def init_db():
    conn = None
    try:
        conn = connect_db()
        cur = conn.cursor()     
        
        with open(DDL_SQL_PATH, 'r', encoding='utf-8') as f:
                sql_script_content = f.read() # 파일 내용을 모두 읽어 문자열로 저장
        cur.executescript(sql_script_content) # 다중 SQL문 실행. 단일은 cur.execute()
        conn.commit()
        
        # 초기 데이터 존재 유무 체크
        # cur.execute("SELECT COUNT(*) FROM survey_responses")
        # count = cur.fetchone()[0]
        # if count == 0:
        #     # 데이터 삽입
        #     cur.execute("INSERT INTO survey_responses (id, gender) VALUES (?, ?)", (1, "여자"))
        #     conn.commit()
        
        #     # 데이터 조회
        #     cur.execute("SELECT * FROM survey_responses")
        #     rows = cur.fetchall()
        #     for row in rows:
        #         print(row)
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def insert_code():
    conn = connect_db()
    cur = conn.cursor()
    # cur.execute("INSERT INTO CODE (CODE_ID, QITEM_NUM, CODE_NM) VALUES (?, ?, ?)", (gender, satisfaction))
    cur.execute("", ())
    conn.commit()
    return
    
def insert_qitem():
    conn = connect_db()
    cur = conn.cursor()
    # cur.execute("INSERT INTO QITEM (QITEM_NUM, QITEM_NM) VALUES (?, ?)", (gender, satisfaction))
    conn.commit()
    return
    
def insert_dgstfn():
    conn = connect_db()
    cur = conn.cursor()
    # cur.execute("""INSERT INTO QITEM (Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13) 
    #             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
    #             (gender, satisfaction))
    conn.commit()
    return

init_db()

