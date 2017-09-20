from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Overridden_On import Overridden_On
from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Fan_On import Exhaust_Fan_On


class Exhaust_Fan_Overridden_On(Overridden_On,Exhaust_Fan_On):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Overridden_On
	
	
