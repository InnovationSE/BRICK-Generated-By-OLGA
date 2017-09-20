from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Building_Static_Pressure_Setpoint import Building_Static_Pressure_Setpoint


class AHU_Building_Static_Pressure_Setpoint(Building_Static_Pressure_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Building_Static_Pressure_Setpoint
	
	
