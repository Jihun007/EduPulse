import sqlite3 as sql
import csv
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def export(db_path, table_name, output_csv_path):    
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

