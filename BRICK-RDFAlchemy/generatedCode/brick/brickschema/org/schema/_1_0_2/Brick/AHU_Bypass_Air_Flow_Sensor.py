from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Bypass_Air_Flow_Sensor import Bypass_Air_Flow_Sensor


class AHU_Bypass_Air_Flow_Sensor(Bypass_Air_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Bypass_Air_Flow_Sensor
	
	
