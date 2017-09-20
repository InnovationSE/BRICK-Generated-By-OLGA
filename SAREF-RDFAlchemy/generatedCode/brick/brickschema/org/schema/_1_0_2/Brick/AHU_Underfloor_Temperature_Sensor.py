from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Underfloor_Temperature_Sensor import Underfloor_Temperature_Sensor


class AHU_Underfloor_Temperature_Sensor(Underfloor_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Underfloor_Temperature_Sensor
	
	
