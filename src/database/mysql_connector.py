import mysql.connector
from mysql.connector import errorcode
from logger import logger

def connect_to_mysql():
    try:
        return mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='your_host',
            database='your_data_base_name',
            port='your_port'
    )

    except mysql.connector.Error as err:
        logger.error(err)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise "Usuario o Password no válido"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise "La base de datos no existe."
        else:
            raise "Se ha producido un error. Por favor contacte a su administrador."
