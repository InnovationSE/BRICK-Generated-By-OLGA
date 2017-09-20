from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fan_Status import Fan_Status
from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop_Status import Start_Stop_Status


class Fan_Start_Stop_Status(Fan_Status,Start_Stop_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fan_Start_Stop_Status
	
	
