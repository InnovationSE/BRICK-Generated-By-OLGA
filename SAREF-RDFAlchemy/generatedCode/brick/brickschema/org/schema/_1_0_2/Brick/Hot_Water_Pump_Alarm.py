from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pump_Alarm import Pump_Alarm
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water


class Hot_Water_Pump_Alarm(Pump_Alarm,Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Pump_Alarm
	
	
