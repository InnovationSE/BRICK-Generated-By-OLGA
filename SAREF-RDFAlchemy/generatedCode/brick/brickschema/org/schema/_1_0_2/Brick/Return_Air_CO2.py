from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Air_CO2 import Air_CO2
from brick.brickschema.org.schema._1_0_2.Brick.Return_Air import Return_Air


class Return_Air_CO2(Air_CO2,Return_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Air_CO2
	
	
