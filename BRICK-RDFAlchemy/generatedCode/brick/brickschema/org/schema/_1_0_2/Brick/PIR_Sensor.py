from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Motion_Sensor import Motion_Sensor


class PIR_Sensor(Motion_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').PIR_Sensor
	
	
