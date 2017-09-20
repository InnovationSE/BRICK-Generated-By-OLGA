from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Economizer_Status import AHU_Economizer_Status
from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Mode_Status import Economizer_Mode_Status


class AHU_Economizer_Mode_Status(AHU_Economizer_Status,Economizer_Mode_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Economizer_Mode_Status
	
	
