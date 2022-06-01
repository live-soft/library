class CreateTables():
    def books(connection):
        mycursor = connection.cursor()

        mycursor.execute("""CREATE TABLE books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            year VARCHAR(255),
            count VARCHAR(255)
        )""")

    def students(connection):
        mycursor = connection.cursor()
        
        mycursor.execute("""CREATE TABLE students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255)
        )""")
        
    def assignedbooks(connection):
        mycursor = connection.cursor()
        
        mycursor.execute("""CREATE TABLE assignedbooks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            book_id VARCHAR(255),
            student_id VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            return_date date NOT NULL
        )""")