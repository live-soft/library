# import mysql.connector
import pymysql.cursors

class Connect():
    def connectionDB():
        db = pymysql.connect(host = 'localhost', user = 'root', password = '', cursorclass = pymysql.cursors.DictCursor)
        # db.close()
        return db

    def connection():
        db = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'library', cursorclass = pymysql.cursors.DictCursor)
        # db.close()
        return db