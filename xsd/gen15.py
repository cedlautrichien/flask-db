import xmlschema
import os

# Charger le XSD
schema = xmlschema.XMLSchema(os.path."CC015C.xsd")
print(schema)

# Générer un XML valide
synthetic_xml = schema.to_dict()  # Renvoie une structure conforme
print(synthetic_xml)
schema.to_xml(synthetic_xml, os.path."CC015C.xml")
