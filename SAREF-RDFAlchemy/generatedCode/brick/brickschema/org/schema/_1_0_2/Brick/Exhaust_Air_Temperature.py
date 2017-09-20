from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Air import Exhaust_Air
from brick.brickschema.org.schema._1_0_2.Brick.Air_Temperature import Air_Temperature


class Exhaust_Air_Temperature(Exhaust_Air,Air_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Air_Temperature
	
	
