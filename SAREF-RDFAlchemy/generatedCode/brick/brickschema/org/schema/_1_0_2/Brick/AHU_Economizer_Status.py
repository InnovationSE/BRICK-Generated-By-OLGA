from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Status import Economizer_Status
from brick.brickschema.org.schema._1_0_2.Brick.Mode_Status import Mode_Status


class AHU_Economizer_Status(Economizer_Status,Mode_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Economizer_Status
	
	
