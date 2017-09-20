from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Mode_Setpoint import Mode_Setpoint


class Dual_Band_Mode_Setpoint(Mode_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Dual_Band_Mode_Setpoint
	
	
