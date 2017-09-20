from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Low_Humidity_Alarm_Setpoint import Low_Humidity_Alarm_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Humidity_Setpoint import CRAC_Humidity_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Low_Humidity_Alarm import CRAC_Low_Humidity_Alarm


class CRAC_Low_Humidity_Alarm_Setpoint(Low_Humidity_Alarm_Setpoint,CRAC_Humidity_Setpoint,CRAC_Low_Humidity_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Low_Humidity_Alarm_Setpoint
	
	
