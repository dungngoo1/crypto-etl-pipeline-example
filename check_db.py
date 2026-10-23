import os
import psycopg2
from dotenv import load_dotenv

def main():
    load_dotenv()
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST","localhost"),
            port=int(os.environ.get("DB_PORT","5432")),
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
        )
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            print(cur.fetchone()[0])
    except KeyError as e:
        print("Thiếu biến môi trường",e)
    except psycopg2.OperationalError as e:
        print("Không kết nối được với DB",e)
    finally:
        if conn is not None:
            conn.close()
            
if __name__ == "__main__":
    main()