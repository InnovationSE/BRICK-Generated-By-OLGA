from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Speed_Reset_Command import Speed_Reset_Command
from brick.brickschema.org.schema._1_0_2.Brick.VFD_Speed_Command import VFD_Speed_Command


class VFD_Speed_Reset_Command(Speed_Reset_Command,VFD_Speed_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Speed_Reset_Command
	
	
