from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure_Setpoint import Static_Pressure_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Air import Exhaust_Air


class Exhaust_Air_Static_Pressure_Setpoint(Static_Pressure_Setpoint,Exhaust_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Air_Static_Pressure_Setpoint
	
	
