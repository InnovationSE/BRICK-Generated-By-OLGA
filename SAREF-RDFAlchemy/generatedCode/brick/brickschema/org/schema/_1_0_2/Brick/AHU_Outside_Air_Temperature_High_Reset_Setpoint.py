from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air_Temperature_High_Reset_Setpoint import Outside_Air_Temperature_High_Reset_Setpoint


class AHU_Outside_Air_Temperature_High_Reset_Setpoint(Outside_Air_Temperature_High_Reset_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Outside_Air_Temperature_High_Reset_Setpoint
	
	
