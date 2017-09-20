from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Request import Cooling_Request


class Cooling_Request_Percent(Cooling_Request):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Request_Percent
	
	
