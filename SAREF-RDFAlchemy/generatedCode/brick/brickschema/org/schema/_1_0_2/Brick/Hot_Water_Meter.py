from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Water_Meter import Water_Meter
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water


class Hot_Water_Meter(Water_Meter,Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Meter
	
	
