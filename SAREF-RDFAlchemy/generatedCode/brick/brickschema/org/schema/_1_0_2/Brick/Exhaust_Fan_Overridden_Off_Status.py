from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Status import Exhaust_Fan_Status
from brick.brickschema.org.schema._1_0_2.Brick.Overridden_Off_Status import Overridden_Off_Status


class Exhaust_Fan_Overridden_Off_Status(Exhaust_Fan_Status,Overridden_Off_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Overridden_Off_Status
	
	
