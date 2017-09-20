from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature import High_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Emergency_Power_Off import Emergency_Power_Off
from brick.brickschema.org.schema._1_0_2.Brick.Temperature_High import Temperature_High


class Emergency_Power_Off_Activated_By_High_Temperature(High_Temperature,Emergency_Power_Off,Temperature_High):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Emergency_Power_Off_Activated_By_High_Temperature
	
	
