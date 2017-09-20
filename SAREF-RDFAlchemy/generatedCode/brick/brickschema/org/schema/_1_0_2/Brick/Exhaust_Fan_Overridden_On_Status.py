from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Overridden_On_Status import Overridden_On_Status
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Status import Exhaust_Fan_Status


class Exhaust_Fan_Overridden_On_Status(Overridden_On_Status,Exhaust_Fan_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Overridden_On_Status
	
	
