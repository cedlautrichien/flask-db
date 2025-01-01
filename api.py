from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)

# defining URL or Path to save our DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# Creating DB instance to reference throughout the code
db = SQLAlchemy(app)


# The following code block is used to create a db instance from flask_sqlalchemy and use it to define our Book table.
# Define a model class
class Book(db.Model):
    # Using ISBN as a primary key
    isbn = db.Column(db.String(150), primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(150))

    @property
    def as_json(self):
        """Returns object data in a serializable format"""
        return {"isbn": self.isbn, "title": self.title, "author": self.author}


# If the DB doesn't exit recreate it else don't overwrite it
if not os.path.exists("books.db"):
    with app.app_context():
        db.create_all()


# @app.route("/add_book_json", methods=["POST"])
# def add_book_json():
# POST request for adding book to DB
#    if request.method == "POST":
#        # Getting user-passed data
#        payload = request.get_json()
#        # Creating a book object
#        book = Book(
#            isbn=payload["isbn"], title=payload["title"], author=payload["author"]
#        )
#        # add new book object to DB
#        db.session.add(book)
#
#        # commit db to save changes
#        db.session.commit()
#
#        # return the same book to let the user know that it has been added to the DB
#        return jsonify(json.dumps(payload))


@app.route("/get_book_json")
def get_book_json():
    # GET request for getting all books from DB
    if request.method == "GET":
        # retrieving all the books from DB
        books = Book.query.all()
        # serializing objects so that we can send them in a JSON object
        serialized_books = [book.as_json for book in books]
        # sending all books back to the client in JSON object
        return jsonify(serialized_books)


@app.route("/get_book_xml")
def get_book_xml():
    xml = "<foo>example</foo>"
    resp = app.make_response(xml)
    resp.mimetype = "text/xml"
    return resp


@app.route("/")
def endpoints():
    return "Endpoints :" + "GET + /get_book_xml" + "GET + /get_book_json"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
