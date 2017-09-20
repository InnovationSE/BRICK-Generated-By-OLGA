from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Communication_Loss_Alarm import Communication_Loss_Alarm


class CRAC_Communication_Loss_Alarm(Communication_Loss_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Communication_Loss_Alarm
	
	
