from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan_Start_Stop_Command import Return_Fan_Start_Stop_Command
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Return_Fan_Command import AHU_Return_Fan_Command


class AHU_Return_Fan_Start_Stop_Command(Return_Fan_Start_Stop_Command,AHU_Return_Fan_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Return_Fan_Start_Stop_Command
	
	
