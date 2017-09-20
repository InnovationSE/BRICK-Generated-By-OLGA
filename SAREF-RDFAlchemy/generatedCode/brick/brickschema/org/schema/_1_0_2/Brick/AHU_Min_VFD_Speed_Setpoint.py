from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Min_VFD_Speed_Setpoint import Min_VFD_Speed_Setpoint


class AHU_Min_VFD_Speed_Setpoint(Min_VFD_Speed_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Min_VFD_Speed_Setpoint
	
	
