from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Max_Load_Setpoint import Max_Load_Setpoint


class Chiller_Max_Load_Setpoint(Max_Load_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chiller_Max_Load_Setpoint
	
	
