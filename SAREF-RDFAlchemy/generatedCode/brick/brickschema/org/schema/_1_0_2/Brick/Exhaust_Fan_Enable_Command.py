from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Command import Exhaust_Fan_Command
from brick.brickschema.org.schema._1_0_2.Brick.Enable_Command import Enable_Command


class Exhaust_Fan_Enable_Command(Exhaust_Fan_Command,Enable_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Enable_Command
	
	
