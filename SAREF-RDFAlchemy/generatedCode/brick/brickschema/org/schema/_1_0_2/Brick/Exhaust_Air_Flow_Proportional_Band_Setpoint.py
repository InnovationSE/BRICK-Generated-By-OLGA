from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Proportional_Band_Setpoint import Proportional_Band_Setpoint


class Exhaust_Air_Flow_Proportional_Band_Setpoint(Proportional_Band_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Air_Flow_Proportional_Band_Setpoint
	
	
