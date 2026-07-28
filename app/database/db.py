import sqlite3
from flask import current_app

def get_db_connection():
    # Toma la ruta de la base de datos desde la configuracion de Flask (.env)
    db_path = current_app.config['DATABASE_URL']
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Para acceder a las columnas por nombre
    return conn