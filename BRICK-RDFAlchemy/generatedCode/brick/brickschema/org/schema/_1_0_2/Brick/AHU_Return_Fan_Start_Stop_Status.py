from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Fan_Start_Stop_Status import AHU_Fan_Start_Stop_Status
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Return_Fan_Status import AHU_Return_Fan_Status
from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan_Start_Stop_Status import Return_Fan_Start_Stop_Status


class AHU_Return_Fan_Start_Stop_Status(AHU_Fan_Start_Stop_Status,AHU_Return_Fan_Status,Return_Fan_Start_Stop_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Return_Fan_Start_Stop_Status
	
	
