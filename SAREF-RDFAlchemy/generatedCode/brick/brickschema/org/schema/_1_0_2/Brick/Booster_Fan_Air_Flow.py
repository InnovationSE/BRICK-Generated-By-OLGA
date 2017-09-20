from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Booster_Fan import Booster_Fan


class Booster_Fan_Air_Flow(Booster_Fan):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Booster_Fan_Air_Flow
	
	
