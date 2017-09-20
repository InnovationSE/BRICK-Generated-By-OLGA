from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Smoke_Detected_Alarm import Smoke_Detected_Alarm


class CRAC_Smoke_Detected_Alarm(Smoke_Detected_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Smoke_Detected_Alarm
	
	
