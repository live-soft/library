from website.mysqlConnect.connect import Connect

class Search():
    def get(value):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM books WHERE title LIKE ('%{value}%') OR author LIKE ('%{value}%')")
            result = cursor.fetchall()

            return result