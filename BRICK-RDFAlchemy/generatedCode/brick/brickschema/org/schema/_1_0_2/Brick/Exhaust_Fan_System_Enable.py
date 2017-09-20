from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.System_Enable import System_Enable
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Enable import Exhaust_Fan_Enable


class Exhaust_Fan_System_Enable(System_Enable,Exhaust_Fan_Enable):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_System_Enable
	
	
