import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv
#Se necesita usar el comando: pip3 install mysql-connector-python
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

database = mysql.connector.connect(
    user='root',
    password=os.getenv("PASSWORD"),
    host='127.0.0.1',
    database='python_db',
    port = '3306'
)