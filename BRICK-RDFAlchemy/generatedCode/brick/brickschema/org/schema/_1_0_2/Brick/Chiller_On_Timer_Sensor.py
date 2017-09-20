from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.On_Timer_Sensor import On_Timer_Sensor


class Chiller_On_Timer_Sensor(On_Timer_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chiller_On_Timer_Sensor
	
	
