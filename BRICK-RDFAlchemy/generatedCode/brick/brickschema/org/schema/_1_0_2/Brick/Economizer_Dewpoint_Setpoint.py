from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Dewpoint_Setpoint import Dewpoint_Setpoint


class Economizer_Dewpoint_Setpoint(Dewpoint_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Dewpoint_Setpoint
	
	
