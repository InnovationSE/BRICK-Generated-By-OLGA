from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan import Exhaust_Fan
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Command import Exhaust_Fan_Command
from brick.brickschema.org.schema._1_0_2.Brick.VFD_Speed_Command import VFD_Speed_Command


class Exhaust_Fan_VFD_Speed_Command(Exhaust_Fan,Exhaust_Fan_Command,VFD_Speed_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_VFD_Speed_Command
	
	
