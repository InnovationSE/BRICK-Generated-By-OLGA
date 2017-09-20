from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Outside_Min_Air_Flow_Setpoint import Outside_Min_Air_Flow_Setpoint


class AHU_Outside_Min_Air_Flow_Setpoint(Outside_Min_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Outside_Min_Air_Flow_Setpoint
	
	
