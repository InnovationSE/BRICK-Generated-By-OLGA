from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_Off import Exhaust_Fan_Off
from brick.brickschema.org.schema._1_0_2.Brick.Overridden_Off import Overridden_Off


class Exhaust_Fan_Overridden_Off(Exhaust_Fan_Off,Overridden_Off):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Overridden_Off
	
	
