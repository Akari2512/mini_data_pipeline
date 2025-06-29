import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

def get_engine():
    try:
        SERVER = os.getenv("DB_SERVER")
        DATABASE = os.getenv("DB_NAME")
        DRIVER = os.getenv("DB_DRIVER")

        connection_string = f"mssql+pyodbc://@{SERVER}/{DATABASE}?trusted_connection=yes&driver={DRIVER}"
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        print(f'[ERROR] Failed to create database engine: {e}')
        return None

