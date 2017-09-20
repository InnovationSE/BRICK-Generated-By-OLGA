from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Alarm_Delay_Setpoint import Alarm_Delay_Setpoint


class Water_System_Alarm_Delay_Setpoint(Alarm_Delay_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Water_System_Alarm_Delay_Setpoint
	
	
