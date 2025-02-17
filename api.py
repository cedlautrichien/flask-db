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


@app.route("/generic_xml")
def get_static_xml():
    message_type = request.args.get("messageType")
    if message_type == "CC014C":
        xml_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><CC014C xmlns:ns3="http://ncts.dgtaxud.ec"><messageSender>swp.transit.agent</messageSender><messageRecipient>NTA.AT</messageRecipient><preparationDateAndTime>2024-12-20T15:11:53</preparationDateAndTime><messageIdentification>100788151153</messageIdentification><messageType>CC014C</messageType><correlationIdentifier>test</correlationIdentifier><TransitOperation><MRN>24AT100000Y5L4I0K0</MRN></TransitOperation><Invalidation><requestDateAndTime>2024-12-20T15:11:53</requestDateAndTime><initiatedByCustoms>0</initiatedByCustoms><justification>darum</justification></Invalidation><CustomsOfficeOfDeparture><referenceNumber>AT100000</referenceNumber></CustomsOfficeOfDeparture><HolderOfTheTransitProcedure><identificationNumber>ATEOS9999999991</identificationNumber><ContactPerson><name>Claus Thorup</name><phoneNumber>2105577890</phoneNumber><eMailAddress>cthor@email.gr</eMailAddress></ContactPerson></HolderOfTheTransitProcedure></CC014C>'
        resp = Response(xml_content, mimetype="application/xml")
        return resp
    else:
        return "No message template found"


@app.route("/austrian_xml")
def get_dynamic_xml():
    message_type = request.args.get("messageType")
    holder_rin = request.args.get("holderRIN")
    mrn = request.args.get("MRN")
    oodep = request.args.get("OoDep")
    holder_eori = request.args.get("holderEORI")
    simplified=request.args.get("simplified")
    authorisation=request.args.get("authorisation")
    oodes=request.args.get("OoDes")
    trader_eori=request.args.get("traderEORI")
    location_type=request.args.get("typeOfLocation")
    qualifier_id=request.args.get("qualifierID")
    trader_rin=request.args.get("traderRIN")
    lid=request.args.get("locationID")

    if message_type == "CC014C":
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

    if message_type == "CC007C":
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
            "arrivalNotificationDateAndTime":"2024-12-20T15:11:53",
            "simplifiedProcedure": simplified,
            "incidentFlag":"0",
            "sequenceNumber": "1",
            "type":"C520",
            "referenceNumber": authorisation,
            "referenceNumber2": oodes,
            "identificationNumber": trader_eori,
            "typeOfLocation":location_type,
            "qualifierOfIdentification":qualifier_id,
            "authorisationNumber":lid
        }

        xml_content = render_template("007C.xml", object=object)
        return Response(xml_content, mimetype="application/xml")

    else:
        return "No message template found"


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
