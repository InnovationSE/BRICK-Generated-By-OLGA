from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fan_Start_Stop_Status import Fan_Start_Stop_Status
from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan_Status import Return_Fan_Status


class Return_Fan_Start_Stop_Status(Fan_Start_Stop_Status,Return_Fan_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Fan_Start_Stop_Status
	
	
