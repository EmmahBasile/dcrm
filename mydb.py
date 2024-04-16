#install mysql on your computer 
#https://dev.mysql.com/donloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
)
# prepare a cursor object
cursorobject = database.cursor()

#create a database
cursorobject.execute("CREATE DATABASE djcrm")

print("All Done")