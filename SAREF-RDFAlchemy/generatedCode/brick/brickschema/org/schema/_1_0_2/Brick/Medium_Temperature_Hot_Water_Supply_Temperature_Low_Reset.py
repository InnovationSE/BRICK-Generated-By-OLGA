from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Low_Temperature import Low_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water_Supply_Temperature import Medium_Temperature_Hot_Water_Supply_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Low import Temperature_Low


class Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset(Low_Temperature,Medium_Temperature_Hot_Water_Supply_Temperature,Temperature_Low):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset
	
	
