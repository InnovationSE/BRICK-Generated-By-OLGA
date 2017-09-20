from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fire_Control_Panel_On_Command import Fire_Control_Panel_On_Command


class AHU_Fire_Control_Panel_On_Command(Fire_Control_Panel_On_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Fire_Control_Panel_On_Command
	
	
