from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Flow_Reset_High_Setpoint import Discharge_Air_Flow_Reset_High_Setpoint


class AHU_Discharge_Air_Flow_Reset_High_Setpoint(Discharge_Air_Flow_Reset_High_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Discharge_Air_Flow_Reset_High_Setpoint
	
	
