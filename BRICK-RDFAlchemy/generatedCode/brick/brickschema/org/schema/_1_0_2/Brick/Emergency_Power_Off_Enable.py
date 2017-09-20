from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Enable import Enable
from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Power_Off import Emergency_Power_Off


class Emergency_Power_Off_Enable(Enable,Emergency_Power_Off):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Emergency_Power_Off_Enable
	
	
