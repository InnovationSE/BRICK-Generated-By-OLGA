from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Status import Exhaust_Fan_Status
from brick.brickschema.org.schema._1_0_2.Brick.Fan_Start_Stop_Status import Fan_Start_Stop_Status


class Exhaust_Fan_Start_Stop_Status(Exhaust_Fan_Status,Fan_Start_Stop_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Start_Stop_Status
	
	
