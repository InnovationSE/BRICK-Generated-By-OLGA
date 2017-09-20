from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Enable_Command import VFD_Enable_Command


class AHU_VFD_Enable_Command(VFD_Enable_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_VFD_Enable_Command
	
	
