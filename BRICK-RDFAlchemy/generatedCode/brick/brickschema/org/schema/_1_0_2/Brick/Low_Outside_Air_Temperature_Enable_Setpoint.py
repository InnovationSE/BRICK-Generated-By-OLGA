from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Setpoint import Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air import Outside_Air


class Low_Outside_Air_Temperature_Enable_Setpoint(Temperature_Setpoint,Outside_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Low_Outside_Air_Temperature_Enable_Setpoint
	
	
