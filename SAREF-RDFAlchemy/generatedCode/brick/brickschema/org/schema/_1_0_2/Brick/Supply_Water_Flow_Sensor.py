from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Water_Flow_Sensor import Water_Flow_Sensor


class Supply_Water_Flow_Sensor(Water_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Water_Flow_Sensor
	
	
