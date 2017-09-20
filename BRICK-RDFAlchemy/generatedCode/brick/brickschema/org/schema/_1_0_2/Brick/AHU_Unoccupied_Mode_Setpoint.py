from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Unoccupied_Mode_Setpoint import Unoccupied_Mode_Setpoint


class AHU_Unoccupied_Mode_Setpoint(Unoccupied_Mode_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Unoccupied_Mode_Setpoint
	
	
