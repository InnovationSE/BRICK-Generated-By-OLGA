from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.System_Enable_Command import System_Enable_Command


class Hot_Water_System_Enable_Command(Hot_Water,System_Enable_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_System_Enable_Command
	
	
