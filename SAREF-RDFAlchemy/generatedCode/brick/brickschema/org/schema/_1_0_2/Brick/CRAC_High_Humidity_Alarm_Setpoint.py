from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CRAC_High_Humidity_Alarm import CRAC_High_Humidity_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Humidity_Setpoint import CRAC_Humidity_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.High_Humidity_Alarm_Setpoint import High_Humidity_Alarm_Setpoint


class CRAC_High_Humidity_Alarm_Setpoint(CRAC_High_Humidity_Alarm,CRAC_Humidity_Setpoint,High_Humidity_Alarm_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_High_Humidity_Alarm_Setpoint
	
	
