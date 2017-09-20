from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Request_Command import Request_Command


class Run_Request_Command(Request_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Run_Request_Command
	
	
