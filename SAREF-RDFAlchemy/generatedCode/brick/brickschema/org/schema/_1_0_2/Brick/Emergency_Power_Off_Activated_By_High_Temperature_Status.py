from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Power_Off_Status import Emergency_Power_Off_Status


class Emergency_Power_Off_Activated_By_High_Temperature_Status(Emergency_Power_Off_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Emergency_Power_Off_Activated_By_High_Temperature_Status
	
	
