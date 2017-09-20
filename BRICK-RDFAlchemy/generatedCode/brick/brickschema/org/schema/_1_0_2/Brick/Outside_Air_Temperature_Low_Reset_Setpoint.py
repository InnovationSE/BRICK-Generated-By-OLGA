from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air import Outside_Air
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Low_Reset_Setpoint import Temperature_Low_Reset_Setpoint


class Outside_Air_Temperature_Low_Reset_Setpoint(Outside_Air,Temperature_Low_Reset_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Outside_Air_Temperature_Low_Reset_Setpoint
	
	
