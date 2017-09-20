from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList



class Tag(rdfSubject):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/BrickFrame#').Tag
	
	
