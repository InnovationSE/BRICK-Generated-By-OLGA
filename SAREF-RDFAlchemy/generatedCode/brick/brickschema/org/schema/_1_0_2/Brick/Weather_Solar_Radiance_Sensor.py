from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Solar_Radiance_Sensor import Solar_Radiance_Sensor


class Weather_Solar_Radiance_Sensor(Solar_Radiance_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Weather_Solar_Radiance_Sensor
	
	
