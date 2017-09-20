from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temperature_High import Temperature_High
from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature import High_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature import Discharge_Air_Temperature


class Discharge_Air_Temperature_High_Limit(Temperature_High,High_Temperature,Discharge_Air_Temperature):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Discharge_Air_Temperature_High_Limit
	
	
