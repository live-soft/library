from website.models.Tables import CreateTables
import pymysql.cursors

class DataBase():
    def create():
        connectionDB = pymysql.connect(host = 'localhost', user = 'root', password = '', cursorclass = pymysql.cursors.DictCursor)
        mycursor = connectionDB.cursor()
        mycursor.execute("show databases")

        populated = filter(lambda c: c['Database'] == 'library', list(mycursor))
        
        if len(list(populated)) == 0:
            mycursor.execute("CREATE DATABASE library")

            connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'library', cursorclass = pymysql.cursors.DictCursor)

            books = CreateTables.books(connection)
            students = CreateTables.students(connection)
            assignedbooks = CreateTables.assignedbooks(connection)

        else:
            from website.mysqlConnect.connect import Connect

            tables = ['assignedbooks', 'books', 'students']

            connection = Connect.connection()
            mycursor = connection.cursor()
            mycursor.execute("Show tables")

            
            for dbTable in list(mycursor):
                tables.remove(dbTable['Tables_in_library'])

            for table in tables:
                if table == 'assignedbooks':
                    assignedbooks = CreateTables.assignedbooks(connection)
                elif table == 'books':
                    books = CreateTables.books(connection)
                elif table == 'students':
                    students = CreateTables.students(connection)