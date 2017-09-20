from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.System_Enable_Command import System_Enable_Command
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Enable_Command import CRAC_Enable_Command


class CRAC_System_Enable_Command(System_Enable_Command,CRAC_Enable_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_System_Enable_Command
	
	
