from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Min_Fresh_Air_Setpoint import Min_Fresh_Air_Setpoint


class AHU_Min_Fresh_Air_Setpoint(Min_Fresh_Air_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Min_Fresh_Air_Setpoint
	
	
