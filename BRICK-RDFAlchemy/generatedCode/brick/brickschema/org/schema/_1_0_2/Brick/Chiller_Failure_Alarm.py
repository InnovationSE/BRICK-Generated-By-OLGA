from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Failure_Alarm import Failure_Alarm


class Chiller_Failure_Alarm(Failure_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chiller_Failure_Alarm
	
	
