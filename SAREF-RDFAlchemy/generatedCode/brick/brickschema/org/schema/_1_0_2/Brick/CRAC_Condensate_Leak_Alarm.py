from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Condensate_Leak_Alarm import Condensate_Leak_Alarm


class CRAC_Condensate_Leak_Alarm(Condensate_Leak_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Condensate_Leak_Alarm
	
	
