from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.System import System
from brick.brickschema.org.schema._1_0_2.Brick.Air_Temperature import Air_Temperature


class Disable_Hot_Water_System_Air_Temperature(System,Air_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Disable_Hot_Water_System_Air_Temperature
	
	
