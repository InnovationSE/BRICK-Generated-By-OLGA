from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature_Alarm_Setpoint import High_Temperature_Alarm_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_High_Temperature_Alarm import CRAC_High_Temperature_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Temperature_Setpoint import CRAC_Temperature_Setpoint


class CRAC_High_Temperature_Alarm_Setpoint(High_Temperature_Alarm_Setpoint,CRAC_High_Temperature_Alarm,CRAC_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_High_Temperature_Alarm_Setpoint
	
	
