
import psycopg2
from psycopg2 import sql, connect
import bcrypt

def get_db_connection():
    try:
        conn = psycopg2.connect("dbname=home-ify user=postgres password=12345")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# def adduser(fullname, email, password):
#     conn = get_db_connection()
#     if not conn:
#         return False
    
#     try:
#         with conn:
#             with conn.cursor() as cur:
#                 query = "INSERT INTO users (fullname, email, password) VALUES (%s, %s, %s)"
#                 cur.execute(query, (fullname, email, password))
#         return True
#     except Exception as e:
#         print(f"Error adding user: {e}")
#         return False
#     finally:
#         conn.close()

def adduser(fullname, email, password):
    conn = get_db_connection()
    if not conn:
        return False

    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        with conn:
            with conn.cursor() as cur:
                query = """
                INSERT INTO users (fullname, email, password)
                VALUES (%s, %s, %s)
                """
                cur.execute(query, (fullname, email, hashed_password))
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False
    finally:
        conn.close()

