from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Building_Exhaust_Fans_Stage_Command import Building_Exhaust_Fans_Stage_Command


class AHU_Building_Exhaust_Fans_Stage_Command(Building_Exhaust_Fans_Stage_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Building_Exhaust_Fans_Stage_Command
	
	
