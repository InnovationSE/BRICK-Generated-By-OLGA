from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Shutdown_Command import Shutdown_Command


class System_Shutdown_Command(Shutdown_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').System_Shutdown_Command
	
	
