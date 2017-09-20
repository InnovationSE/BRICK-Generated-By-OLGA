from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating import Heating


class Heating_Temperature(Heating):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Temperature
	
	
