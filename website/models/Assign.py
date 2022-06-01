from website.mysqlConnect.connect import Connect

class Assign():
    def getById(id):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM `assignedbooks` WHERE book_id={ id }')
            result = cursor.fetchall()

            return result

    def getByStudentId(id, bookId):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM `assignedbooks` WHERE student_id={ id } AND book_id={ bookId }')
            result = cursor.fetchall()

            return result

    def hasRetur(books):
        returId = []

        for key in books:
            returData = Assign.getById(key['id'])

            if len(returData) > 0:
                if returData[0]['book_id'] not in returId:
                    returId.append(int(returData[0]['book_id']))

        return returId
    
    def set(data):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO assignedbooks (student_id, book_id, first_name, last_name, return_date) VALUES (%s, %s, %s, %s, %s)"
            val = (data['student_id'], data['book_id'], data['first_name'], data['last_name'], data['return_date'])
            cursor.execute(sql, val)

        connection.commit()

    def remove(id):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM `assignedbooks` WHERE id={ id }')
        
        connection.commit()