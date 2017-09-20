from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fans_Stage_Command import Fans_Stage_Command


class Building_Exhaust_Fans_Stage_Command(Fans_Stage_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Building_Exhaust_Fans_Stage_Command
	
	
