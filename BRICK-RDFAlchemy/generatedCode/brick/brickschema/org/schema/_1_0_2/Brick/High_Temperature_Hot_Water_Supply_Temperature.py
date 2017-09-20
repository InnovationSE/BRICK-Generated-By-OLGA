from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Water_Temperature import Supply_Water_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Water_Supply_Temperature import Water_Supply_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature_Hot_Water import High_Temperature_Hot_Water


class High_Temperature_Hot_Water_Supply_Temperature(Supply_Water_Temperature,Water_Supply_Temperature,High_Temperature_Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').High_Temperature_Hot_Water_Supply_Temperature
	
	
