from flask import Flask, request, Response, render_template, jsonify
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


@app.route("/get_static_xml")
def get_static_xml():
    type = request.args.get("type")
    if type == "014C":
        xml_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><CC014C xmlns:ns2="urn:eds:datamodel:EDS:EDS_EXTENSIONS:1" xmlns:ns3="http://ncts.dgtaxud.ec"><Extensions><SequenceNumeric>1</SequenceNumeric><Key>HolderOfTheTransitProcedureRIN</Key><Value>ATRIN4952418247</Value><DataType>text</DataType></Extensions><messageSender>swp.transit.agent</messageSender><messageRecipient>NTA.AT</messageRecipient><preparationDateAndTime>2024-12-20T15:11:53</preparationDateAndTime><messageIdentification>100788_151153</messageIdentification><messageType>CC014C</messageType><correlationIdentifier>test</correlationIdentifier><TransitOperation><MRN>24AT100000Y5L4I0K0</MRN></TransitOperation><Invalidation><requestDateAndTime>2024-12-20T15:11:53</requestDateAndTime><initiatedByCustoms>0</initiatedByCustoms><justification>darum</justification></Invalidation><CustomsOfficeOfDeparture><referenceNumber>AT100000</referenceNumber></CustomsOfficeOfDeparture><HolderOfTheTransitProcedure><identificationNumber>ATEOS9999999991</identificationNumber><ContactPerson><name>Claus Thorup</name><phoneNumber>2105577890</phoneNumber><eMailAddress>cthor@email.gr</eMailAddress></ContactPerson></HolderOfTheTransitProcedure></CC014C>'
        resp = Response(xml_content, mimetype="application/xml")
        return resp
    else:
        return "No message template found"


@app.route("/get_dynamic_xml")
def get_dynamic_xml():
    type = request.args.get("type")
    if type == "014C":
        object = {
            "SequenceNumeric": "1",
            "Key": "HolderOfTheTransitProcedureRIN",
            "Value": "ATRIN4952418247",
            "DataType": "text",
            "messageSender": "swp.transit.agent",
            "messageRecipient": "NTA.AT",
            "preparationDateAndTime": "2024-12-20T15:11:53",
            "messageIdentification": "100788_151153",
            "messageType": "CC014C",
            "correlationIdentifier": "test",
            "MRN": "24AT100000Y5L4I0K0",
            "requestDateAndTime": "2024-12-20T15:11:53",
            "initiatedByCustoms": "0",
            "justification": "darum",
            "referenceNumber": "AT100000",
            "identificationNumber": "ATEOS9999999991",
            "name": "Claus Thorup",
            "phoneNumber": "2105577890",
            "eMailAddress": "cthor@email.gr",
        }

        xml_content = render_template("014C.xml", object=object)
        return Response(xml_content, mimetype="application/xml")

    else:
        return "No message template found"


@app.route("/post_json_data", methods=["POST"])
def post_json_data():
    type = request.args.get("type")
    if type == "014C":

        if request.is_json:
            object = request.get_json()
        else:
            return jsonify({"error": "Invalid requested, expected JSON"}), 400

        xml_content = render_template("014C.xml", object=object)
        return Response(xml_content, mimetype="application/xml")

    else:
        return "No message template found"


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
