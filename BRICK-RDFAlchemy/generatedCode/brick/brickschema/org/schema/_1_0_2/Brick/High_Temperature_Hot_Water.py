from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temperature_High import Temperature_High
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature import High_Temperature


class High_Temperature_Hot_Water(Temperature_High,Hot_Water,High_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').High_Temperature_Hot_Water
	
	
