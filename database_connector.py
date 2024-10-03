from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.host = os.getenv('DB_HOST') 
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.port = os.getenv('DB_PORT', 3306)  # Puerto por defecto si no está definido

    def connect(self, database):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=database
            )
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
    

    def execute_query(self, db_name, query):
        self.connect(db_name)
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return result
    