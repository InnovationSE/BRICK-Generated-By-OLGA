from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Mixed_Air_Damper_Position_Command import Mixed_Air_Damper_Position_Command


class AHU_Mixed_Air_Damper_Position_Command(Mixed_Air_Damper_Position_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Mixed_Air_Damper_Position_Command
	
	
