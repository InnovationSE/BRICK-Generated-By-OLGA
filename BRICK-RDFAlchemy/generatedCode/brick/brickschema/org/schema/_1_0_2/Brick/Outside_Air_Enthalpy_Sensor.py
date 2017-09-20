from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air import Outside_Air
from brick.brickschema.org.schema._1_0_2.Brick.Outside_Enthalpy_Sensor import Outside_Enthalpy_Sensor


class Outside_Air_Enthalpy_Sensor(Outside_Air,Outside_Enthalpy_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Outside_Air_Enthalpy_Sensor
	
	
