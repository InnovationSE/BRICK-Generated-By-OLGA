from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Damper_Position import Damper_Position


class Bypass_Damper_Position(Damper_Position):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Bypass_Damper_Position
	
	
