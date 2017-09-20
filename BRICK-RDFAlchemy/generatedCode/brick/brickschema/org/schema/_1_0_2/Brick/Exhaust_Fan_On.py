from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.On import On
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan import Exhaust_Fan


class Exhaust_Fan_On(On,Exhaust_Fan):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_On
	
	
