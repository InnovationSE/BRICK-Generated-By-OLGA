from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer import Economizer
from brick.brickschema.org.schema._1_0_2.Brick.Air_Temperature import Air_Temperature


class Economizer_Differential_Air_Temperature(Economizer,Air_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Differential_Air_Temperature
	
	
