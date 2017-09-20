from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Energy_Meter import Energy_Meter


class Peak_Energy_Today_Meter(Energy_Meter):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Peak_Energy_Today_Meter
	
	
