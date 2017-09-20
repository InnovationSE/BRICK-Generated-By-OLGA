from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Current_Limit_Setpoint import Current_Limit_Setpoint


class VFD_Current_Limit_Setpoint(Current_Limit_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Current_Limit_Setpoint
	
	
