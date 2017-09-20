from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Direction_Command import Direction_Command


class Run_Direction_Command(Direction_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Run_Direction_Command
	
	
