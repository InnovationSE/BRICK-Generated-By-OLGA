from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Head_Pressure_Alarm import High_Head_Pressure_Alarm


class CRAC_High_Head_Pressure_Alarm(High_Head_Pressure_Alarm):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_High_Head_Pressure_Alarm
	
	
