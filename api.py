from flask import (
    Flask,
    request,
    Response,
    render_template,
    send_from_directory,
)
from flask_sqlalchemy import SQLAlchemy

from datetime import date, datetime
import random, string


# functions to retrieve date, time and generate a reference
def today():
    today = date.today()
    return today


def prepdt():
    today = date.today()
    today_string = today.strftime("%d%m%Y")
    return today_string


def now():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    return dt_string


def randomref():
    characters = string.ascii_uppercase + string.digits
    generated_string = "".join(random.choices(characters, k=12))
    return generated_string


app = Flask(__name__)

# defining URL or Path to save our DB
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"
# Creating DB instance to reference throughout the code
# db = SQLAlchemy(app)


# If the DB doesn't exist recreate it else don't overwrite it
# if not os.path.exists("messages.db"):
#   with app.app_context():
#       db.create_all()


@app.route("/CC014C")
def get_CC014C():
    # retrieve arguments from request
    holder_rin = request.args.get("holderRIN")
    mrn = request.args.get("MRN")
    oodep = request.args.get("OoDep")
    holder_eori = request.args.get("holderEORI")

    # retrieve date and time and generate reference
    now_retrieve = now()
    randomref_generate = randomref()
    prepdt_generate = prepdt()

    object = {
        "PrepDT": prepdt_generate,
        "ICRef": randomref_generate,
        "SequenceNumeric": "1",
        "Key": "HolderOfTheTransitProcedureRIN",
        "Value": holder_rin,
        "DataType": "text",
        "messageSender": "Wirtschaftsbeteiligter",
        "messageRecipient": "NTA.AT",
        "preparationDateAndTime": now_retrieve,
        "messageIdentification": randomref_generate,
        "messageType": "CC014C",
        "correlationIdentifier": "test",
        "MRN": mrn,
        "requestDateAndTime": now_retrieve,
        "initiatedByCustoms": "0",
        "justification": "test",
        "referenceNumber": oodep,
        "identificationNumber": holder_eori,
        "name": "test",
        "phoneNumber": "123456780",
        "eMailAddress": "test@test.com",
    }

    xml_content = render_template("014C.xml", object=object)
    return Response(xml_content, mimetype="application/xml")


@app.route("/CC007C")
def get_CC007C():
    # retrieve arguments from request
    trader_rin = request.args.get("traderRIN")
    mrn = request.args.get("MRN")
    authorisation_C522 = request.args.get("authorisationID_C522")
    oodes = request.args.get("OoDes")
    trader_eori = request.args.get("traderEORI")
    lid = request.args.get("locationID")

    # retrieve date and time and generate reference
    now_retrieve = now()
    randomref_generate = randomref()
    prepdt_generate = prepdt()

    object = {
        "PrepDT": prepdt_generate,
        "ICRef": randomref_generate,
        "SequenceNumeric": "1",
        "Key": "TraderAtDestinationRIN",
        "Value": trader_rin,
        "DataType": "text",
        "messageSender": "Wirtschaftsbeteiligter",
        "messageRecipient": "NTA.AT",
        "preparationDateAndTime": now_retrieve,
        "messageIdentification": randomref_generate,
        "messageType": "CC007C",
        "correlationIdentifier": "test",
        "MRN": mrn,
        "arrivalNotificationDateAndTime": now_retrieve,
        "simplifiedProcedure": "1",
        "incidentFlag": "0",
        "sequenceNumber1": "1",
        "type": "C522",
        "referenceNumber1": authorisation_C522,
        "referenceNumber2": oodes,
        "identificationNumber": trader_eori,
        "typeOfLocation": "B",
        "qualifierOfIdentification": "Y",
        "authorisationNumber": lid,
    }

    xml_content = render_template("007C.xml", object=object)
    return Response(xml_content, mimetype="application/xml")


@app.route("/CC007C_TIR")
def get_CC007C_TIR():
    # retrieve arguments from request
    trader_rin = request.args.get("traderRIN")
    mrn = request.args.get("MRN")
    authorisation_C520 = request.args.get("authorisationID_C520")
    authorisation_C522 = request.args.get("authorisationID_C522")
    oodes = request.args.get("OoDes")
    trader_eori = request.args.get("traderEORI")
    lid = request.args.get("locationID")

    # retrieve date and time and generate reference
    now_retrieve = now()
    randomref_generate = randomref()
    prepdt_generate = prepdt()

    object = {
        "PrepDT": prepdt_generate,
        "ICRef": randomref_generate,
        "SequenceNumeric": "1",
        "Key": "TraderAtDestinationRIN",
        "Value": trader_rin,
        "DataType": "text",
        "messageSender": "Wirtschaftsbeteiligter",
        "messageRecipient": "NTA.AT",
        "preparationDateAndTime": now_retrieve,
        "messageIdentification": randomref_generate,
        "messageType": "CC007C",
        "correlationIdentifier": "test",
        "MRN": mrn,
        "arrivalNotificationDateAndTime": now_retrieve,
        "simplifiedProcedure": "1",
        "incidentFlag": "0",
        "sequenceNumber1": "1",
        "type1": "C520",
        "referenceNumber1": authorisation_C520,
        "sequenceNumber2": "2",
        "type2": "C522",
        "referenceNumber2": authorisation_C522,
        "referenceNumber3": oodes,
        "identificationNumber": trader_eori,
        "typeOfLocation": "B",
        "qualifierOfIdentification": "Y",
        "authorisationNumber": lid,
    }

    xml_content = render_template("007C_TIR.xml", object=object)
    return Response(xml_content, mimetype="application/xml")


@app.route("/CC044C")
def get_CC044C():
    # retrieve arguments from request
    oodes = request.args.get("OoDes")
    trader_eori = request.args.get("traderEORI")
    trader_rin = request.args.get("traderRIN")
    mrn = request.args.get("MRN")

    # retrieve date and time and generate reference
    now_retrieve = now()
    randomref_generate = randomref()
    today_retrieve = today()
    prepdt_generate = prepdt()

    object = {
        "PrepDT": prepdt_generate,
        "ICRef": randomref_generate,
        "SequenceNumeric": "1",
        "Key": "TraderAtDestinationRIN",
        "Value": trader_rin,
        "DataType": "text",
        "messageSender": "Wirtschaftsbeteiligter",
        "messageRecipient": "NTA.AT",
        "preparationDateAndTime": now_retrieve,
        "messageIdentification": randomref_generate,
        "messageType": "CC044C",
        "correlationIdentifier": "test",
        "MRN": mrn,
        "referenceNumber": oodes,
        "identificationNumber": trader_eori,
        "conform": "1",
        "unloadingCompletion": "1",
        "unloadingDate": today_retrieve,
        "stateOfSeals": "1",
    }

    xml_content = render_template("044C.xml", object=object)
    return Response(xml_content, mimetype="application/xml")


@app.route("/")
def home():
    return render_template("index.html")


# Serve static files (Swagger UI assets)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static/swagger-ui", filename)


# Serve OpenAPI YAML file
@app.route("/openapi.yaml")
def openapi_spec():
    return send_from_directory("static", "openapi.yaml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
