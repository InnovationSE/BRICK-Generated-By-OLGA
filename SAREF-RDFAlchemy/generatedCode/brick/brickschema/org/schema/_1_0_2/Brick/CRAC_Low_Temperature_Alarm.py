from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Low_Temperature_Alarm import Low_Temperature_Alarm


class CRAC_Low_Temperature_Alarm(Low_Temperature_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Low_Temperature_Alarm
	
	
