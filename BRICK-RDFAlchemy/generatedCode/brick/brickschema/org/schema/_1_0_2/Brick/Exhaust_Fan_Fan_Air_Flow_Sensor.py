from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fan_Air_Flow_Sensor import Fan_Air_Flow_Sensor


class Exhaust_Fan_Fan_Air_Flow_Sensor(Fan_Air_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Fan_Air_Flow_Sensor
	
	
