from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fan_Speed_Reset_Command import Fan_Speed_Reset_Command


class Supply_Fan_Fan_Speed_Reset_Command(Fan_Speed_Reset_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Fan_Fan_Speed_Reset_Command
	
	
