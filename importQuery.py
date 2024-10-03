from database_connector import DatabaseConnector
import mysql.connector

import logging

class ExecuteSQL:
    def __init__(self) -> None:
        self.conection = DatabaseConnector()
        self.file = "scripts/example.sql"
        # Configuración del logging
        logging.basicConfig(filename='logs/execute_sql.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


    def execute_query_file(self, arr_bd):
        """Ejecuta las consultas SQL en el archivo para múltiples bases de datos.

        Args:
            arr_bd (list): Lista con los nombres de las bases de datos donde se ejecutará el script.
        """
        logging.info(f"Iniciando ejecución del archivo '{self.file}' en las bases de datos: {arr_bd}")

        # Lee el archivo SQL
        with open(self.file, 'r') as file:
            sqlscript = file.read()

        try:
            # Ejecuta el script en cada base de datos
            for db in arr_bd:
                self.conection.connect(db)
                if not self.conection.conn:
                    logging.error(f"No se pudo establecer la conexión con la base de datos '{db}'")
                    continue

                # Divide las consultas si hay más de una (usando punto y coma para separar)
                queries = sqlscript.split(';')
                for query in queries:
                    query = query.strip()  # Elimina espacios en blanco
                    if query:  # Solo si la consulta no está vacía
                        cursor = self.conection.conn.cursor()
                        try:
                            # Identifica el tipo de consulta (SELECT o no)
                            if query.lower().startswith('select'):
                                cursor.execute(query)
                                result = cursor.fetchall()
                                logging.info(f"Resultado de la consulta SELECT en '{db}': {result}")
                                print(f"{db} => {result}")
                            else:
                                cursor.execute(query)
                                self.conection.conn.commit()  # Realiza commit si es un INSERT
                                logging.info(f"Consulta ejecutada en '{db}': {query}")
                                print(f"{db} => Consulta ejecutada: {query}")
                        except mysql.connector.Error as error:
                            logging.error(f"Error al ejecutar la consulta en '{db}': {error}")
                            print(f"Error al ejecutar la consulta en '{db}': {error}")
                        finally:
                            cursor.close()

        except mysql.connector.Error as error:
            logging.error(f"Error general al ejecutar el archivo SQL: {error}")
            print(f"Error general al ejecutar el archivo SQL: {error}")
        finally:
            logging.info(f"Finalizada la ejecución del archivo '{self.file}'")
            file.close()