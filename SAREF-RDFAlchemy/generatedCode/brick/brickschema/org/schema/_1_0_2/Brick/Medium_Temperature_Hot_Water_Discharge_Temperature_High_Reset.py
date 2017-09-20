from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature_Hot_Water_Discharge_Temperature import High_Temperature_Hot_Water_Discharge_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water_Discharge_Temperature import Medium_Temperature_Hot_Water_Discharge_Temperature


class Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset(High_Temperature_Hot_Water_Discharge_Temperature,Medium_Temperature_Hot_Water_Discharge_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset
	
	
