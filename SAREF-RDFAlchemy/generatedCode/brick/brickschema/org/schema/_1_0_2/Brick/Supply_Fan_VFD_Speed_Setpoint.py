from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Speed_Setpoint import VFD_Speed_Setpoint


class Supply_Fan_VFD_Speed_Setpoint(VFD_Speed_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Fan_VFD_Speed_Setpoint
	
	
