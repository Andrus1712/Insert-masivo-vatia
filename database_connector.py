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
        self.file = "scripts/example.sql"

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
        result = cursor.rowcount()
        cursor.close()
        self.conn.close()
        return result
    
    def execute_query_from_file(self, db_name, sql_file):
        """Ejecuta una consulta SQL a partir de un archivo.

        Args:
            database (str): Nombre de la base de datos.
            sql_file (str): Ruta al archivo .sql.
        """
        if not self.conn:
            self.connect(db_name)

        if self.conn:
            cursor = self.conn.cursor()
            with open(sql_file, 'r') as file:
                query = file.read()
                try:
                    cursor.execute(query)
                    result = cursor.fetchall()
                except mysql.connector.Error as error:
                    print(f"Error al ejecutar la consulta: {error}")
                finally:
                    cursor.close()
            return result
        else:
            print("No se pudo establecer la conexión a la base de datos.")
            
    def execute_query_file(self, arr_bd):
        with open(self.file, 'r') as file:
            sqlscript = file.read()
        try:
            for db in arr_bd:
                result = self.execute_query(db, sqlscript)
                print(f"{db} => {result}")
        except mysql.connector.Error as error:
            print(f"Error al ejecutar la consulta: {error}")
        finally:
            file.close()
        