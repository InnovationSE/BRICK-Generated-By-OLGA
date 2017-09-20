from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Outside_Air_Flow_Setpoint import Economizer_Outside_Air_Flow_Setpoint


class AHU_Economizer_Outside_Air_Flow_Setpoint(Economizer_Outside_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Economizer_Outside_Air_Flow_Setpoint
	
	
