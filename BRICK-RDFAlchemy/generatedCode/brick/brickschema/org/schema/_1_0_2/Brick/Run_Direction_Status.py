from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Run_Status import Run_Status
from brick.brickschema.org.schema._1_0_2.Brick.Direction_Status import Direction_Status


class Run_Direction_Status(Run_Status,Direction_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Run_Direction_Status
	
	
