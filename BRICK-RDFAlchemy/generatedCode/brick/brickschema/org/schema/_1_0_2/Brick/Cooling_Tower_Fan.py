from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CWS import CWS


class Cooling_Tower_Fan(CWS):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Tower_Fan
	
	
