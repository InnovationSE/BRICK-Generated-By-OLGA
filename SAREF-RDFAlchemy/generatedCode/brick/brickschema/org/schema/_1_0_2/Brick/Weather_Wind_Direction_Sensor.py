from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Wind_Direction_Sensor import Wind_Direction_Sensor


class Weather_Wind_Direction_Sensor(Wind_Direction_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Weather_Wind_Direction_Sensor
	
	
