from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Mode_Command import Mode_Command


class Maintenance_Mode_Command(Mode_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Maintenance_Mode_Command
	
	
