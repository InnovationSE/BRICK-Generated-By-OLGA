from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Air_Flow_Setpoint import Air_Flow_Setpoint


class Ventilation_Air_Flow_Ratio_Limit_Setpoint(Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Ventilation_Air_Flow_Ratio_Limit_Setpoint
	
	