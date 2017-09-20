from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Command import Exhaust_Fan_Command
from brick.brickschema.org.schema._1_0_2.Brick.Fire_Control_Panel_On_Command import Fire_Control_Panel_On_Command


class Exhaust_Fan_Fire_Control_Panel_On_Command(Exhaust_Fan_Command,Fire_Control_Panel_On_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Fire_Control_Panel_On_Command
	
	
