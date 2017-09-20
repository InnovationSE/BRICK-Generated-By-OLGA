from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VAV_Zone_Temperature_Sensor import VAV_Zone_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Zone_Air_Temperature_Sensor import Zone_Air_Temperature_Sensor


class VAV_Zone_Air_Temperature_Sensor(VAV_Zone_Temperature_Sensor,Zone_Air_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Zone_Air_Temperature_Sensor
	
	
