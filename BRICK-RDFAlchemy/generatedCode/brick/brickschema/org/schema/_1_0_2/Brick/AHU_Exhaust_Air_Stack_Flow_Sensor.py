from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Air_Stack_Flow_Sensor import Exhaust_Air_Stack_Flow_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Exhaust_Air_Flow_Sensor import AHU_Exhaust_Air_Flow_Sensor


class AHU_Exhaust_Air_Stack_Flow_Sensor(Exhaust_Air_Stack_Flow_Sensor,AHU_Exhaust_Air_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Exhaust_Air_Stack_Flow_Sensor
	
	
