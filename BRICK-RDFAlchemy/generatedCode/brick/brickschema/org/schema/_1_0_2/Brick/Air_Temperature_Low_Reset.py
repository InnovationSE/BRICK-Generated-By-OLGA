from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Low import Temperature_Low
from brick.brickschema.org.schema._1_0_2.Brick.Air_Temperature import Air_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Low_Temperature import Low_Temperature


class Air_Temperature_Low_Reset(Temperature_Low,Air_Temperature,Low_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Air_Temperature_Low_Reset
	
	
