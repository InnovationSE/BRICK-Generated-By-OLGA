from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Air_Temperature_High_Limit_Alarm import Return_Air_Temperature_High_Limit_Alarm


class AHU_Return_Air_Temperature_High_Limit_Alarm(Return_Air_Temperature_High_Limit_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Return_Air_Temperature_High_Limit_Alarm
	
	
