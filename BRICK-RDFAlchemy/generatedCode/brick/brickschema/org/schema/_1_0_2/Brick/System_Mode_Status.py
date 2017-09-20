from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Mode_Status import Mode_Status
from brick.brickschema.org.schema._1_0_2.Brick.System_Status import System_Status


class System_Mode_Status(Mode_Status,System_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').System_Mode_Status
	
	
