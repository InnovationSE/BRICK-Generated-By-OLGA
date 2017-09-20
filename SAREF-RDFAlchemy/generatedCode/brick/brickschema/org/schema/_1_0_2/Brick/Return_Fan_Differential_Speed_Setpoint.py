from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Differential_Speed_Setpoint import Differential_Speed_Setpoint


class Return_Fan_Differential_Speed_Setpoint(Differential_Speed_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Fan_Differential_Speed_Setpoint
	
	
