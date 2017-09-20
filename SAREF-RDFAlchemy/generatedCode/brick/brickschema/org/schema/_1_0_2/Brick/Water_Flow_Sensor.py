from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Flow_Sensor import Flow_Sensor


class Water_Flow_Sensor(Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Water_Flow_Sensor
	
	
