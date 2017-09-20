from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Energy_Storage import Energy_Storage


class Thermal_Energy_Storage(Energy_Storage):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Thermal_Energy_Storage
	
	
