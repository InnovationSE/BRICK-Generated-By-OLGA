from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.On import On


class Overridden_On(On):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Overridden_On
	
	
