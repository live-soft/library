from website.mysqlConnect.connect import Connect

class Student():
    def get():
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            result = cursor.fetchall()

            return result
    
    def getByEmail(email):
        students = Student.get()

        return list(filter(lambda x: x['email'] == email, students))

    def set(data):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)"
            val = (data['firstname'], data['lastname'], data['email'])
            cursor.execute(sql, val)

        connection.commit()

    def remove(id):
        connection = Connect.connection()
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM `students` WHERE id={ id }')

        connection.commit()