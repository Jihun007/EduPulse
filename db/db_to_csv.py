import sqlite3 as sql
import csv
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def export_db_to_csv(db_path, table_name, output_csv_path):    
    try:
        # 데이터베이스에 연결
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # 테이블의 모든 데이터를 조회
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # 데이터가 없을 경우
        if not rows:
            print(f"테이블 '{table_name}'에 데이터가 없습니다.")
            return

        # 테이블의 열(컬럼) 이름을 가져옴
        column_names = [description[0] for description in cursor.description]

        # CSV 파일로 저장
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(column_names)
            
            if table_name == 'DGSTFN':
                for row in rows:
                    numeric_id = row[0]
                    # 숫자 ID에 'R'을 붙여서 텍스트 ID 생성
                    r_id = f"R{numeric_id}"

                    # 나머지 데이터와 합쳐서 새로운 행 생성
                    processed_row = (r_id,) + row[1:]
                    csv_writer.writerow(processed_row)            
            else:
                csv_writer.writerows(rows)

        print(f"'{db_path}' 데이터베이스의 '{table_name}' 테이블 데이터가 '{output_csv_path}' 파일로 성공적으로 저장되었습니다.")

    except sql.Error as e:
        print(f"SQLite 오류 발생: {e}")
    except IOError as e:
        print(f"파일 입출력 오류 발생: {e}")
    finally:
        # 연결 종료
        if conn:
            conn.close()

# --- 사용 예시 ---
if __name__ == "__main__":
    
    """
        db_path (str): SQLite 데이터베이스 파일의 경로. 예: 'mydatabase.db'
        table_name (str): CSV로 내보낼 테이블의 이름. 예: 'users'
        output_csv_path (str): 생성될 CSV 파일의 경로. 예: 'users_data.csv'
    """
    
    DATABASE_FILE = 'survey.db'     # SQLite DB 파일명
    TABLE_NAME = 'DGSTFN'            # CSV로 내보낼 테이블명
    OUTPUT_CSV_FILE = TABLE_NAME + '.csv' # 생성될 CSV 파일명
    OUTPUT_FOLDER = 'data\survey'
        
    sys.path.append(PROJECT_ROOT)  
    output_full_path = os.path.join(PROJECT_ROOT, OUTPUT_FOLDER, OUTPUT_CSV_FILE)
    # 폴더가 없으면 생성
    os.makedirs(os.path.dirname(output_full_path), exist_ok=True)

    export_db_to_csv(DATABASE_FILE, TABLE_NAME, output_full_path)