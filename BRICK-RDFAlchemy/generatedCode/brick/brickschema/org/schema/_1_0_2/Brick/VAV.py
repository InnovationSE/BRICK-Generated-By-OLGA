from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Terminal_Unit import Terminal_Unit


class VAV(Terminal_Unit):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV
	
	
