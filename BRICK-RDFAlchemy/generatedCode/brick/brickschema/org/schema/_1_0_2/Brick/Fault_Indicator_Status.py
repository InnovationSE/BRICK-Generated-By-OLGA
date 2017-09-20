from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fault_Status import Fault_Status


class Fault_Indicator_Status(Fault_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fault_Indicator_Status
	
	
