# import mysql.connector
from website.models.config import host,user,password,cursorclass,database
import pymysql.cursors

class Connect():
    def connectionDB():
        return pymysql.connect(host = host, user = user, password = password, cursorclass = cursorclass)

    def connection():
        return pymysql.connect(host = host, user = user, password = password, database = database, cursorclass = cursorclass)