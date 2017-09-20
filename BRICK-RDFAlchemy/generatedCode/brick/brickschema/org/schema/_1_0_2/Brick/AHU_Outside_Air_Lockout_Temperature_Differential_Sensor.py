from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Outside_Air_Temperature_Sensor import AHU_Outside_Air_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air_Lockout_Temperature_Differential_Sensor import Outside_Air_Lockout_Temperature_Differential_Sensor


class AHU_Outside_Air_Lockout_Temperature_Differential_Sensor(AHU_Outside_Air_Temperature_Sensor,Outside_Air_Lockout_Temperature_Differential_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Outside_Air_Lockout_Temperature_Differential_Sensor
	
	
