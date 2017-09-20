from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Overridden_Status import Overridden_Status


class Overridden_Off_Status(Overridden_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Overridden_Off_Status
	
	
