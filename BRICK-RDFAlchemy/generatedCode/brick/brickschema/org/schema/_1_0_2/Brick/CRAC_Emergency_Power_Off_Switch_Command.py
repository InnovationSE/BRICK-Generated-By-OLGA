from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Power_Off_Switch_Command import Emergency_Power_Off_Switch_Command
from brick.brickschema.org.schema._1_0_2.Brick.CRAC_Emergency_Power_Off_Command import CRAC_Emergency_Power_Off_Command


class CRAC_Emergency_Power_Off_Switch_Command(Emergency_Power_Off_Switch_Command,CRAC_Emergency_Power_Off_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Emergency_Power_Off_Switch_Command
	
	
