from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_System_Enable_Command import Chilled_Water_System_Enable_Command


class CWS_Chilled_Water_System_Enable_Command(Chilled_Water_System_Enable_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CWS_Chilled_Water_System_Enable_Command
	
	
