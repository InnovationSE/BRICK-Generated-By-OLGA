from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer import Economizer
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature import Supply_Air_Temperature


class Economizer_Supply_Air_Temperature_Proportional_Band(Economizer,Supply_Air_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Supply_Air_Temperature_Proportional_Band
	
	
