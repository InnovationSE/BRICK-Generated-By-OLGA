from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Change_Filter_Alarm import Change_Filter_Alarm


class AHU_Change_Filter_Alarm(Change_Filter_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Change_Filter_Alarm
	
	
