from flask import (
    Flask,
    request,
    Response,
    render_template,
    jsonify,
    send_from_directory,
)
from flask_sqlalchemy import SQLAlchemy

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
    message_type = request.args.get("messageType")
    holder_rin = request.args.get("holderRIN")
    mrn = request.args.get("MRN")
    oodep = request.args.get("OoDep")
    holder_eori = request.args.get("holderEORI")

    object = {
        "SequenceNumeric": "1",
        "Key": "HolderOfTheTransitProcedureRIN",
        "Value": holder_rin,
        "DataType": "text",
        "messageSender": "Wirtschaftsbeteiligter",
        "messageRecipient": "NTA.AT",
        "preparationDateAndTime": "2024-12-20T15:11:53",
        "messageIdentification": "100788_151153",
        "messageType": message_type,
        "correlationIdentifier": "test",
        "MRN": mrn,
        "requestDateAndTime": "2024-12-20T15:11:53",
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
    simplified = request.args.get("simplified")
    authorisation_C520 = request.args.get("authorisationID_C520")
    oodes = request.args.get("OoDes")
    trader_eori = request.args.get("traderEORI")
    location_type = request.args.get("typeOfLocation")
    qualifier_id = request.args.get("qualifierID")
    trader_rin = request.args.get("traderRIN")
    lid = request.args.get("locationID")
    message_type = request.args.get("messageType")
    mrn = request.args.get("MRN")

    object = {
        "SequenceNumeric": "1",
        "Key": "HolderOfTheTransitProcedureRIN",
        "Value": trader_rin,
        "DataType": "text",
        "messageSender": "Wirtschaftsbeteiligter",
        "messageRecipient": "NTA.AT",
        "preparationDateAndTime": "2024-12-20T15:11:53",
        "messageIdentification": "100788_151153",
        "messageType": message_type,
        "correlationIdentifier": "test",
        "MRN": mrn,
        "arrivalNotificationDateAndTime": "2024-12-20T15:11:53",
        "simplifiedProcedure": simplified,
        "incidentFlag": "0",
        "sequenceNumber1": "1",
        "type": "C520",
        "referenceNumber1": authorisation_C520,
        "referenceNumber2": oodes,
        "identificationNumber": trader_eori,
        "typeOfLocation": location_type,
        "qualifierOfIdentification": qualifier_id,
        "authorisationNumber": lid,
    }

    xml_content = render_template("007C.xml", object=object)
    return Response(xml_content, mimetype="application/xml")


@app.route("/CC007C_TIR")
def get_CC007C_TIR():
    simplified = request.args.get("simplified")
    authorisation_C520 = request.args.get("authorisationID_C520")
    authorisation_C522 = request.args.get("authorisationID_C522")
    oodes = request.args.get("OoDes")
    trader_eori = request.args.get("traderEORI")
    location_type = request.args.get("typeOfLocation")
    qualifier_id = request.args.get("qualifierID")
    trader_rin = request.args.get("traderRIN")
    lid = request.args.get("locationID")
    message_type = request.args.get("messageType")
    mrn = request.args.get("MRN")

    object = {
        "SequenceNumeric": "1",
        "Key": "HolderOfTheTransitProcedureRIN",
        "Value": trader_rin,
        "DataType": "text",
        "messageSender": "Wirtschaftsbeteiligter",
        "messageRecipient": "NTA.AT",
        "preparationDateAndTime": "2024-12-20T15:11:53",
        "messageIdentification": "100788_151153",
        "messageType": message_type,
        "correlationIdentifier": "test",
        "MRN": mrn,
        "arrivalNotificationDateAndTime": "2024-12-20T15:11:53",
        "simplifiedProcedure": simplified,
        "incidentFlag": "0",
        "sequenceNumber1": "1",
        "type1": "C520",
        "referenceNumber1": authorisation_C520,
        "sequenceNumber2": "2",
        "type2": "C522",
        "referenceNumber2": authorisation_C522,
        "referenceNumber3": oodes,
        "identificationNumber": trader_eori,
        "typeOfLocation": location_type,
        "qualifierOfIdentification": qualifier_id,
        "authorisationNumber": lid,
    }

    xml_content = render_template("007C_TIR.xml", object=object)
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
