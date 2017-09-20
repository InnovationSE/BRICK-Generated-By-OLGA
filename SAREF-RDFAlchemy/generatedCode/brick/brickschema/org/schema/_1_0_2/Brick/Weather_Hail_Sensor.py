from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hail_Sensor import Hail_Sensor


class Weather_Hail_Sensor(Hail_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Weather_Hail_Sensor
	
	
