from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Filter_Reset_Command import Filter_Reset_Command


class VFD_Filter_Reset_Command(Filter_Reset_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Filter_Reset_Command
	
	
