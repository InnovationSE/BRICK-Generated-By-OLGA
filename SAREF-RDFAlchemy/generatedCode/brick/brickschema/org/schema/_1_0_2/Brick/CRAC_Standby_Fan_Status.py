from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Standby_Fan_Status import Standby_Fan_Status


class CRAC_Standby_Fan_Status(Standby_Fan_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Standby_Fan_Status
	
	
