from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Acceleration_Time_Setpoint import Acceleration_Time_Setpoint


class VFD_Acceleration_Time_Setpoint(Acceleration_Time_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Acceleration_Time_Setpoint
	
	
