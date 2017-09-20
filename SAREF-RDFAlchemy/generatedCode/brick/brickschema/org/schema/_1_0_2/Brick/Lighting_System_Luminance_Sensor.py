from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Luminance_Sensor import Luminance_Sensor


class Lighting_System_Luminance_Sensor(Luminance_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Lighting_System_Luminance_Sensor
	
	
