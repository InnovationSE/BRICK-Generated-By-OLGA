from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Speed_Command import VFD_Speed_Command
from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan_Command import Return_Fan_Command


class Return_Fan_VFD_Speed_Command(VFD_Speed_Command,Return_Fan_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Fan_VFD_Speed_Command
	
	
