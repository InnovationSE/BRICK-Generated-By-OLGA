from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Air_Flow_Sensor import Air_Flow_Sensor


class Fan_Air_Flow_Sensor(Air_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fan_Air_Flow_Sensor
	
	
