from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Command import Exhaust_Fan_Command
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Disable import Exhaust_Fan_Disable
from brick.brickschema.org.schema._1_0_2.Brick.Disable_Command import Disable_Command


class Exhaust_Fan_Disable_Command(Exhaust_Fan_Command,Exhaust_Fan_Disable,Disable_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Disable_Command
	
	
