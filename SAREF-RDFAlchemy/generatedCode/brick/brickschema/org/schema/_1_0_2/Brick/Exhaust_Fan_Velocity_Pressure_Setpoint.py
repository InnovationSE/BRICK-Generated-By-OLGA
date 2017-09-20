from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Velocity_Pressure_Setpoint import Velocity_Pressure_Setpoint


class Exhaust_Fan_Velocity_Pressure_Setpoint(Velocity_Pressure_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Velocity_Pressure_Setpoint
	
	
