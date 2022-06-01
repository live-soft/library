from flask import Blueprint,render_template,request,redirect,flash
from asyncio.windows_events import NULL
from website.models.Book import Book
from website.models.Student import Student
from website.models.Assign import Assign

single = Blueprint('single', __name__)

@single.route('/single/<id>')
def index(id):
    book = Book.getById(id)
    students = Student.get()
    assign = Assign.getById(id)

    return render_template('single/single.html', singleBook=book, students=students, assignedBooks=assign)

@single.route('/unassign', methods=['POST'])
def unassign():
    id = request.form['ids'].split('-')
    book = Book.getById(id[1])
    count = int(book[0]['count']) + 1

    Book.updateCount(count, book[0]['id'])
    Assign.remove(id[0])

    return redirect(f'/single/{ id[1] }')

@single.route('/newAssign', methods=['POST'])
def newAssign():
    studentData = request.form
    studentInfo = studentData['student'].split('-')
    bookId = studentData['bookId']
    book = Book.getById(bookId)
    count = NULL

    if int(book[0]['count']) > 0:
        count = int(book[0]['count']) - 1

    data = {
        'student_id': studentInfo[0],
        'book_id': book[0]['id'],
        'first_name': studentInfo[1],
        'last_name': studentInfo[2],
        'return_date': studentData['refund_date'],
    }

    assign = Assign.getByStudentId(studentInfo[0], bookId)

    if (int(len(assign)) == 0) and (count >= 0) and (int(book[0]['count']) > 0):
        Assign.set(data)
        Book.updateCount(count, book[0]['id'])
    elif len(assign) > 0:
        flash('You have already taken this book!', category='error')
    elif int(book[0]['count']) == 0:
        flash('No book found in library!', category='error')

    return redirect(f'/single/{ bookId }')