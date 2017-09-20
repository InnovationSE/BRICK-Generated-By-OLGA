from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Low_Air_Temperature_Enable import Low_Air_Temperature_Enable


class Low_Air_Temperature_Enable_Differential(Low_Air_Temperature_Enable):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Low_Air_Temperature_Enable_Differential
	
	
