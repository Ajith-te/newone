from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive=True)


@app.route('/books')
def book():
    books = [{'name': 'book1', 'author': 'abc1',
              'cover': 'https://www.shutterstock.com/image-vector/modern-vector-abstract-book-cover-260nw-246688564.jpg'},
             {'name': 'book2', 'author': 'abc2',
              'cover': 'https://www.shutterstock.com/image-vector/modern-vector-abstract-book-cover-260nw-246688564.jpg'},
             {'name': 'book3', 'author': 'abc3',
              'cover': 'https://www.shutterstock.com/image-vector/modern-vector-abstract-book-cover-260nw-246688564.jpg'}]
    return render_template('book.html', books=books)


app.run(debug=True)
