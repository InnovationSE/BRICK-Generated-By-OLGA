from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Timer_Sensor import Timer_Sensor


class On_Timer_Sensor(Timer_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').On_Timer_Sensor
	
	
