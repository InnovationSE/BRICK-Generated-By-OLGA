from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Mixed_Air_Temperature_Setpoint import Mixed_Air_Temperature_Setpoint


class AHU_Mixed_Air_Temperature_Setpoint(Mixed_Air_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Mixed_Air_Temperature_Setpoint
	
	
