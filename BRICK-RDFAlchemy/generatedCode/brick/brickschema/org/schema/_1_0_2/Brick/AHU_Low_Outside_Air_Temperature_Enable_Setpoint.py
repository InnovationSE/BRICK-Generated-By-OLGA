from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Low_Outside_Air_Temperature_Enable_Setpoint import Low_Outside_Air_Temperature_Enable_Setpoint


class AHU_Low_Outside_Air_Temperature_Enable_Setpoint(Low_Outside_Air_Temperature_Enable_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Low_Outside_Air_Temperature_Enable_Setpoint
	
	
