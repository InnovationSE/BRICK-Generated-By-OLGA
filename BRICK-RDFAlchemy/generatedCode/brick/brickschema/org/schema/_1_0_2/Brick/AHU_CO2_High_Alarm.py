from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CO2_High_Alarm import CO2_High_Alarm


class AHU_CO2_High_Alarm(CO2_High_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_CO2_High_Alarm
	
	
