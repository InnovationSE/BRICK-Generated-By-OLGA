from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Box_Mode import Box_Mode


class Box_Operating_Mode(Box_Mode):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Box_Operating_Mode
	
	
