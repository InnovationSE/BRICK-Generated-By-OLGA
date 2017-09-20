from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Damper_Position_Setpoint import Damper_Position_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Outside_Air import Outside_Air


class Outside_Air_Damper_Min_Position_Setpoint(Damper_Position_Setpoint,Outside_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Outside_Air_Damper_Min_Position_Setpoint
	
	
