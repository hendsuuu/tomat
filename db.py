import mysql.connector
from mysql.connector import Error

# Konfigurasi koneksi ke database MySQL
db_config = {
    'user': 'root',                
    'password': '',                
    'host': '127.0.0.1',           
    'port': 3306,                   
    'database': 'dbtomat'          
}

# Fungsi untuk membuat koneksi ke database
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")  # Menggunakan print untuk debug
        return None

# Fungsi untuk memeriksa koneksi
def check_db_connection():
    conn = get_db_connection()
    if conn and conn.is_connected():
        conn.close()
        return True
    return False

