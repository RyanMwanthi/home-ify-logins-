
import psycopg2
from psycopg2 import sql, connect
import bcrypt

conn = psycopg2.connect("dbname=home-ify user=postgres password=12345")
cur = conn.cursor()


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
            hashed_password = hash_password(password).decode('utf-8')  # Decode to store as a string
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
            return "Error adding user"
    finally:
            conn.close()
    
    # conn = get_db_connection()
    # if not conn:
    #     return False

    # try:
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
    #     with conn:
    #         with conn.cursor() as cur:
    #             query = """
    #             INSERT INTO users (fullname, email, password)
    #             VALUES (%s, %s, %s)
    #             """
    #             cur.execute(query, (fullname, email, hashed_password))
    #     return True
    # except Exception as e:
    #     print(f"Error adding user: {e}")
    #     return False
    # finally:
    #     conn.close()


# def hash_password(password):
#     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# def verify_password(stored_password, provided_password):
#     return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

# def login_user():
#     conn = get_db_connection()
#     if not conn:
#         return None

#     try:
#         with conn:
#             with conn.cursor() as cur:
#                 query = "SELECT email, password FROM users"
#                 cur.execute(query)
#                 data = cur.fetchall()
#                 return data
#     except Exception as e:
#         print(f"Error fetching users: {e}")
#         return None
#     finally:
#         conn.close()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(stored_password, provided_password):
    # Ensure stored_password is in bytes
    if isinstance(stored_password, str):
        stored_password = stored_password.encode('utf-8')
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

def login_user():
    conn = get_db_connection()
    if not conn:
        return None

    try:
        with conn:
            with conn.cursor() as cur:
                query = "SELECT email, password FROM users"
                cur.execute(query)
                data = cur.fetchall()
                return data
    except Exception as e:
        print(f"Error fetching users: {e}")
        return None
    finally:
        conn.close()