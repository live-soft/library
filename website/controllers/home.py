from flask import Blueprint,render_template,request,url_for,redirect,flash
from website.models.Book import Book
from website.models.Student import Student
from website.models.Assign import Assign
from website.models.Search import Search

home = Blueprint('home', __name__)

@home.route('/')
def index():
    books = Book.get()
    students = Student.get()
    hasRetur = Assign.hasRetur(books)

    return render_template('home.html', books=books, students=students, hasRetur=hasRetur)

@home.route('/searchbook', methods=['POST'])
def searchbook():
    searchValue = request.form['searchValue']
    books = Search.get(searchValue)
    students = Student.get()
    hasRetur = Assign.hasRetur(books)

    return render_template('home.html', books=books, students=students, hasRetur=hasRetur, searchValue=searchValue)

@home.route('/newstudent', methods=['POST'])
def newstudent():
    hasStudent = Student.getByEmail(request.form['email'])

    if len(hasStudent) == 0:
        Student.set(request.form)
    else:
        flash('This student is already in the database!', category='error')
        
    return redirect(url_for('home.index'))

@home.route('/deleteStudent', methods=['POST'])
def deleteStudent():
    Student.remove(request.form['id'])

    return redirect(url_for('home.index'))

@home.route('/newbook', methods=['POST'])
def newbook():
    hasBook = Book.filter(request.form)

    if len(hasBook) == 0:
        Book.set(request.form)
    else:
        flash('You have already has this book!', category='error')

    return redirect(url_for('home.index'))

@home.route('/delete', methods=['POST'])
def delete():
    Book.remove(request.form['id'])

    return redirect(url_for('home.index'))