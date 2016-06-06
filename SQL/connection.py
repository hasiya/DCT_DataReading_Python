import mysql.connector
from mysql.connector import errorcode
from pip._vendor.requests.packages.urllib3.connection import port_by_scheme

try:
    cnx = mysql.connector.connect(user='root',
                                  password='nandadasa1',
                                  host='127.0.0.1',
                                  port='3306',
                                  database='data')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
