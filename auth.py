import bcrypt
from db import get_db_connection

# Fungsi untuk menambahkan pengguna baru ke database
def add_user(username, password):
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        conn.close()

# Fungsi untuk memverifikasi kredensial pengguna
def verify_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result:
            stored_password = result[0].encode('utf-8')
            return bcrypt.checkpw(password.encode('utf-8'), stored_password)
        return False
    finally:
        cursor.close()
        conn.close()
