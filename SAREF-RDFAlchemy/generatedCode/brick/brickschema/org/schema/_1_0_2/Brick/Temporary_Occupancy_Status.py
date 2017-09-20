from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Occupancy_Status import Occupancy_Status


class Temporary_Occupancy_Status(Occupancy_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Temporary_Occupancy_Status
	
	
