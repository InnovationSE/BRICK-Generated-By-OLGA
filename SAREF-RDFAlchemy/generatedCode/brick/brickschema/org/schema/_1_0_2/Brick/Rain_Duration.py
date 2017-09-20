from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Rain import Rain


class Rain_Duration(Rain):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Rain_Duration
	
	
