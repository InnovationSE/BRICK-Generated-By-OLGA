from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Bypass_Damper_Command import Exhaust_Bypass_Damper_Command


class AHU_Exhaust_Bypass_Damper_Command(Exhaust_Bypass_Damper_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Exhaust_Bypass_Damper_Command
	
	
