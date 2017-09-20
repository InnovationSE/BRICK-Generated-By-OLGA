from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Reset_Setpoint import Reset_Setpoint


class Temperature_High_Reset_Setpoint(Reset_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Temperature_High_Reset_Setpoint
	
	
