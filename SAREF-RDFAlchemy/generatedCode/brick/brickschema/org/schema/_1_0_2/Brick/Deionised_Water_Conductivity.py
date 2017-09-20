from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Deionised_Water import Deionised_Water


class Deionised_Water_Conductivity(Deionised_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Deionised_Water_Conductivity
	
	
