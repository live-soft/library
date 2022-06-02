from website.models.Tables import CreateTables

class DataBase():
    def create():
        from website.mysqlConnect.connect import Connect

        mycursor = Connect.connectionDB().cursor()
        mycursor.execute("show databases")

        populated = filter(lambda c: c['Database'] == 'library', list(mycursor))
        
        if len(list(populated)) == 0:
            mycursor.execute("CREATE DATABASE library")

            connection = Connect.connection();

            CreateTables.books(connection)
            CreateTables.students(connection)
            CreateTables.assignedbooks(connection)

        else:
            tables = ['assignedbooks', 'books', 'students']

            connection = Connect.connection()
            mycursor = connection.cursor()
            mycursor.execute("Show tables")
            
            for dbTable in list(mycursor):
                tables.remove(dbTable['Tables_in_library'])

            for table in tables:
                if table == 'assignedbooks':
                    CreateTables.assignedbooks(connection)
                elif table == 'books':
                    CreateTables.books(connection)
                elif table == 'students':
                    CreateTables.students(connection)