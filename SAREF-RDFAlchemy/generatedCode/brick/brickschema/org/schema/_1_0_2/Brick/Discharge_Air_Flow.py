from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Air_Flow import Air_Flow


class Discharge_Air_Flow(Air_Flow):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Discharge_Air_Flow
	
	
