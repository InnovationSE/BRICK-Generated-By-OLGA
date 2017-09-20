from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pre_Filter_Status import Pre_Filter_Status
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Filter_Status import AHU_Filter_Status


class AHU_Pre_Filter_Status(Pre_Filter_Status,AHU_Filter_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Pre_Filter_Status
	
	
