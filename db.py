import mysql.connector
import os
#Se necesita usar el comando: pip3 install mysql-connector-python

database = mysql.connector.connect(
    user='root',
    password=os.getenv("PASSWORD"),
    host='127.0.0.1',
    database='python_db',
    port = '3306'
)