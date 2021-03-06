from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pump_Alarm import Pump_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Alarm_Delay_Setpoint import Alarm_Delay_Setpoint


class Pump_Alarm_Delay_Setpoint(Pump_Alarm,Alarm_Delay_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Pump_Alarm_Delay_Setpoint
	
	
