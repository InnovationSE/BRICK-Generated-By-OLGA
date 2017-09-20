from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Flow import Supply_Air_Flow


class Average_Supply_Air_Flow(Supply_Air_Flow):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Average_Supply_Air_Flow
	
	