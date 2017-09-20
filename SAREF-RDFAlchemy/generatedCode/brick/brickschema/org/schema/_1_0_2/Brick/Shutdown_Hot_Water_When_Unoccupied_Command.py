from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Shutdown_Command import Shutdown_Command


class Shutdown_Hot_Water_When_Unoccupied_Command(Hot_Water,Shutdown_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Shutdown_Hot_Water_When_Unoccupied_Command
	
	
