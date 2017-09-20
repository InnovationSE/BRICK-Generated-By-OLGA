from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Humidity_Sensor import CRAC_Humidity_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Zone_Humidity_Sensor import Zone_Humidity_Sensor


class CRAC_Zone_Humidity_Sensor(CRAC_Humidity_Sensor,Zone_Humidity_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Zone_Humidity_Sensor
	
	
