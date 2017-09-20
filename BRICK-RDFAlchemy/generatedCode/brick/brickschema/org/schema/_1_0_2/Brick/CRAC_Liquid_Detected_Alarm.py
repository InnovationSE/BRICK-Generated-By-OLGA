from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Liquid_Detected_Alarm import Liquid_Detected_Alarm


class CRAC_Liquid_Detected_Alarm(Liquid_Detected_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Liquid_Detected_Alarm
	
	
