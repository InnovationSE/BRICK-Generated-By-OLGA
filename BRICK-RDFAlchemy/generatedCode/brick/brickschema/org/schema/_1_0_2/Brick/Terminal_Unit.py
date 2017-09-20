from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.HVAC import HVAC


class Terminal_Unit(HVAC):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Terminal_Unit
	
	
