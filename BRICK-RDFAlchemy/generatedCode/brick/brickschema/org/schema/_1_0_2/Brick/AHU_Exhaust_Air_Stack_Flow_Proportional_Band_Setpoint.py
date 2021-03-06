from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Air_Stack_Flow_Proportional_Band_Setpoint import Exhaust_Air_Stack_Flow_Proportional_Band_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Exhaust_Air_Stack_Flow_Setpoint import AHU_Exhaust_Air_Stack_Flow_Setpoint


class AHU_Exhaust_Air_Stack_Flow_Proportional_Band_Setpoint(Exhaust_Air_Stack_Flow_Proportional_Band_Setpoint,AHU_Exhaust_Air_Stack_Flow_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Exhaust_Air_Stack_Flow_Proportional_Band_Setpoint
	
	
