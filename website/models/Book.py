from website.mysqlConnect.connect import Connect

class Book():
    def get():
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM books')
            result = cursor.fetchall()

            return result

    def getById(id):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM `books` WHERE id={ id }')
            result = cursor.fetchall()

            return result

    def set(data):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            sql = 'INSERT INTO books (title, author, year, count) VALUES (%s, %s, %s, %s)'
            val = (data['title'], data['author'], data['year'], data['count'])
            cursor.execute(sql, val)

        connection.commit()

    def updateCount(count, bookId):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f'UPDATE `books` SET count={ count } WHERE id={ bookId }')

        connection.commit()

    def remove(id):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM `books` WHERE id={ id }')

        connection.commit()

    def filter(data):
        books = Book.get()

        return list(filter(lambda x: (x['title'] == data['title'] and x['author'] == data['author'] and x['year'] == data['year']), books))