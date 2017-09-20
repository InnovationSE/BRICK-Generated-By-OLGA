from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Pump_Alarm import Hot_Water_Pump_Alarm


class HWS_Hot_Water_Pump_Alarm(Hot_Water_Pump_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HWS_Hot_Water_Pump_Alarm
	
	
