from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.System_Status import System_Status


class FCU_System_Status(System_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_System_Status
	
	
