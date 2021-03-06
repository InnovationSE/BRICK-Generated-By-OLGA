from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Humidity_Setpoint import Humidity_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.High_Humidity_Alarm import High_Humidity_Alarm


class High_Humidity_Alarm_Setpoint(Humidity_Setpoint,High_Humidity_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').High_Humidity_Alarm_Setpoint
	
	
