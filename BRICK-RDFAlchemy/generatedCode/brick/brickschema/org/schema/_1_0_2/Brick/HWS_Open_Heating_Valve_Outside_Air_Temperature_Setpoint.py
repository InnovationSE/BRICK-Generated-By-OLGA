from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Open_Heating_Valve_Outside_Air_Temperature_Setpoint import Open_Heating_Valve_Outside_Air_Temperature_Setpoint


class HWS_Open_Heating_Valve_Outside_Air_Temperature_Setpoint(Open_Heating_Valve_Outside_Air_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HWS_Open_Heating_Valve_Outside_Air_Temperature_Setpoint
	
	
