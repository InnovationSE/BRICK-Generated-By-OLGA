from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pressure_Setpoint import Pressure_Setpoint


class Static_Pressure_Setpoint(Pressure_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Static_Pressure_Setpoint
	
	
