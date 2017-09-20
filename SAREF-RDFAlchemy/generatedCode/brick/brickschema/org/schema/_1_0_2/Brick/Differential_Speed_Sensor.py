from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Speed_Sensor import Speed_Sensor


class Differential_Speed_Sensor(Speed_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Differential_Speed_Sensor
	
	
