from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Equipment import Equipment


class Power_System(Equipment):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Power_System
	
	
