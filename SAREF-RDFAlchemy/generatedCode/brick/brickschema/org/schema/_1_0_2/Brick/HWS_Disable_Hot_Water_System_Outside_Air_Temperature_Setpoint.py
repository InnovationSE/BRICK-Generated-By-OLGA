from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Disable_Hot_Water_System_Outside_Air_Temperature_Setpoint import Disable_Hot_Water_System_Outside_Air_Temperature_Setpoint


class HWS_Disable_Hot_Water_System_Outside_Air_Temperature_Setpoint(Disable_Hot_Water_System_Outside_Air_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HWS_Disable_Hot_Water_System_Outside_Air_Temperature_Setpoint
	
	
