from flask import Flask, request, jsonify, make_response, render_template
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
class XML_Message(db.Model):
    # Using ISBN as a primary key
    SequenceNumeric = db.Column(db.String(150), primary_key=True)
    Key = db.Column(db.String(150))
    Value = db.Column(db.String(150))
    DataType = db.Column(db.String(150))
    messageSender = db.Column(db.String(150))
    messageRecipient = db.Column(db.String(150))
    preparationDateAndTime = db.Column(db.String(150))
    messageIdentification = db.Column(db.String(150))
    messageType = db.Column(db.String(150))
    correlationIdentifier = db.Column(db.String(150))
    MRN = db.Column(db.String(150))
    requestDateAndTime = db.Column(db.String(150))
    initiatedByCustoms = db.Column(db.String(150))
    justification = db.Column(db.String(150))
    referenceNumber = db.Column(db.String(150))
    identificationNumber = db.Column(db.String(150))
    name = db.Column(db.String(150))
    phoneNumber = db.Column(db.String(150))
    eMailAddress = db.Column(db.String(150))

    @property
    def as_json(self):
        """Returns object data in a serializable format"""
        return {"isbn": self.isbn, "title": self.title, "author": self.author}


# If the DB doesn't exist recreate it else don't overwrite it
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


# @app.route("/get_book_json")
# def get_book_json():
# GET request for getting all books from DB
#    if request.method == "GET":
# retrieving all the books from DB
#       books = Book.query.all()
# serializing objects so that we can send them in a JSON object
#      serialized_books = [book.as_json for book in books]
# sending all books back to the client in JSON object
#     return jsonify(serialized_books)


@app.route("/get_message_xml/014C/")
def get_014C():
    xml = '<CC014C xmlns:ns2="urn:eds:datamodel:EDS:EDS_EXTENSIONS:1" xmlns:ns3="http://ncts.dgtaxud.ec"><Extensions><SequenceNumeric>1</SequenceNumeric><Key>HolderOfTheTransitProcedureRIN</Key><Value>ATRIN4952418247</Value><DataType>text</DataType></Extensions><messageSender>swp.transit.agent</messageSender><messageRecipient>NTA.AT</messageRecipient><preparationDateAndTime>2024-12-20T15:11:53</preparationDateAndTime><messageIdentification>100788_151153</messageIdentification><messageType>CC014C</messageType><correlationIdentifier>test</correlationIdentifier><TransitOperation><MRN>24AT100000Y5L4I0K0</MRN></TransitOperation><Invalidation><requestDateAndTime>2024-12-20T15:11:53</requestDateAndTime><initiatedByCustoms>0</initiatedByCustoms><justification>darum</justification></Invalidation><CustomsOfficeOfDeparture><referenceNumber>AT100000</referenceNumber></CustomsOfficeOfDeparture><HolderOfTheTransitProcedure><identificationNumber>ATEOS9999999991</identificationNumber><ContactPerson><name>Claus Thorup</name><phoneNumber>2105577890</phoneNumber><eMailAddress>cthor@email.gr</eMailAddress></ContactPerson></HolderOfTheTransitProcedure></CC014C>'

    resp = app.make_response(xml)
    resp.mimetype = "text/xml"
    return resp


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
