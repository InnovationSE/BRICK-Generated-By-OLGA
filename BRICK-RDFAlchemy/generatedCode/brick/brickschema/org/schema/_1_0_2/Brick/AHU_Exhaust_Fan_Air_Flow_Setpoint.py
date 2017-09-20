from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Air_Flow_Setpoint import Exhaust_Fan_Air_Flow_Setpoint


class AHU_Exhaust_Fan_Air_Flow_Setpoint(Exhaust_Fan_Air_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Exhaust_Fan_Air_Flow_Setpoint
	
	
