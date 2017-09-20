from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Dewpoint_Setpoint import Economizer_Dewpoint_Setpoint


class Economizer_Enable_Fixed_Dewpoint_Setpoint(Economizer_Dewpoint_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Enable_Fixed_Dewpoint_Setpoint
	
	
