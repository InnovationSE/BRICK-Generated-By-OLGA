from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Status import Status


class Emergency_Push_Button_Status(Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Emergency_Push_Button_Status
	
	