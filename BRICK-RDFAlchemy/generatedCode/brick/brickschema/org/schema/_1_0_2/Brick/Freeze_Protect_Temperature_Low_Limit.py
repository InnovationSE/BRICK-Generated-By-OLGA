from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Freeze import Freeze
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Low import Temperature_Low
from brick.brickschema.org.schema._1_0_2.Brick.Low_Temperature import Low_Temperature


class Freeze_Protect_Temperature_Low_Limit(Freeze,Temperature_Low,Low_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Freeze_Protect_Temperature_Low_Limit
	
	
