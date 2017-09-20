from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Reset_Command import Reset_Command


class Speed_Reset_Command(Reset_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Speed_Reset_Command
	
	
