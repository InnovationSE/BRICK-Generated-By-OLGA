from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Command import Command
from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Air_Flow import Emergency_Air_Flow


class Emergency_Air_Flow_Command(Command,Emergency_Air_Flow):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Emergency_Air_Flow_Command
	
	
