from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Direction_Sensor import Direction_Sensor


class Wind_Direction_Sensor(Direction_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Wind_Direction_Sensor
	
	
