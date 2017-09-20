from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air import Outside_Air
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint import Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water


class Enable_Hot_Water_System_Outside_Air_Temperature_Setpoint(Outside_Air,Temperature_Setpoint,Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Enable_Hot_Water_System_Outside_Air_Temperature_Setpoint
	
	
