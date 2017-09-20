from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Tower_Fan_Speed_Setpoint import Cooling_Tower_Fan_Speed_Setpoint


class Water_System_Cooling_Tower_Fan_Speed_Setpoint(Cooling_Tower_Fan_Speed_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Water_System_Cooling_Tower_Fan_Speed_Setpoint
	
	
