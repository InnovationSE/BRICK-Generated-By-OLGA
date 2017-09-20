from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Low_Temperature_Alarm import CRAC_Low_Temperature_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Temperature_Setpoint import CRAC_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Low_Temperature_Alarm_Setpoint import Low_Temperature_Alarm_Setpoint


class CRAC_Low_Temperature_Alarm_Setpoint(CRAC_Low_Temperature_Alarm,CRAC_Temperature_Setpoint,Low_Temperature_Alarm_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Low_Temperature_Alarm_Setpoint
	
	
