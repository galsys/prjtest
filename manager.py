# db 정보를 전달해 줍니다.
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine, text


load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

def get_engine():
    engine = create_engine(DATABASE_URL, echo=True, isolation_level="AUTOCOMMIT")
    return engine

if __name__ == "__main__":
    try:
        print("Connected to PostgreSQL database")
        
        # SQL 쿼리 실행
        engine = get_engine()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM marcap limit 10;"))
            
            for row in result:
                print(row)
                
    except Exception as e:
        print("Error:", e)

    finally:
        if engine is not None:
            # 연결 닫기
            engine.dispose()
            print("Connection closed")

