from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Dual_Band_Mode_Setpoint import Dual_Band_Mode_Setpoint


class AHU_Dual_Band_Mode_Setpoint(Dual_Band_Mode_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Dual_Band_Mode_Setpoint
	
	
