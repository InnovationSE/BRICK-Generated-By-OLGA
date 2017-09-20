from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Air_Temperature import Air_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature import High_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_High import Temperature_High


class Air_Temperature_High_Reset(Air_Temperature,High_Temperature,Temperature_High):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Air_Temperature_High_Reset
	
	
