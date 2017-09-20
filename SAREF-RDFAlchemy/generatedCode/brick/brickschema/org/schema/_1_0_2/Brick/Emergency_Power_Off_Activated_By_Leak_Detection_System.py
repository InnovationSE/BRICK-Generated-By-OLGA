from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.System import System
from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Power_Off import Emergency_Power_Off


class Emergency_Power_Off_Activated_By_Leak_Detection_System(System,Emergency_Power_Off):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Emergency_Power_Off_Activated_By_Leak_Detection_System
	
	