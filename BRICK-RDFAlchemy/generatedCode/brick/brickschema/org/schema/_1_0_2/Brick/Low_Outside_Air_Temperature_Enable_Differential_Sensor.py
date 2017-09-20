from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Differential_Temperature_Sensor import Differential_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air_Temperature_Sensor import Outside_Air_Temperature_Sensor


class Low_Outside_Air_Temperature_Enable_Differential_Sensor(Differential_Temperature_Sensor,Outside_Air_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Low_Outside_Air_Temperature_Enable_Differential_Sensor
	
	
