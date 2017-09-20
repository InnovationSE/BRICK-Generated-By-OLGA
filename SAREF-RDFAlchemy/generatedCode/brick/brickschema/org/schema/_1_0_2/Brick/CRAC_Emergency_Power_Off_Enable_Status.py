from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Power_Off_Enable_Status import Emergency_Power_Off_Enable_Status


class CRAC_Emergency_Power_Off_Enable_Status(Emergency_Power_Off_Enable_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Emergency_Power_Off_Enable_Status
	
	
