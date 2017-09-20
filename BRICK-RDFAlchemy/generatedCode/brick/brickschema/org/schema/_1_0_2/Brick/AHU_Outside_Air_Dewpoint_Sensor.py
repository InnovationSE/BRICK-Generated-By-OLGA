from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air_Dewpoint_Sensor import Outside_Air_Dewpoint_Sensor


class AHU_Outside_Air_Dewpoint_Sensor(Outside_Air_Dewpoint_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Outside_Air_Dewpoint_Sensor
	
	
