from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Supply_Temperature_Low_Reset_Setpoint import Hot_Water_Supply_Temperature_Low_Reset_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water import Medium_Temperature_Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Water_Temperature_Setpoint import Discharge_Water_Temperature_Setpoint


class Medium_Temperature_Hot_Water_Discharge_Temperature_Low_Reset_Setpoint(Hot_Water_Supply_Temperature_Low_Reset_Setpoint,Medium_Temperature_Hot_Water,Discharge_Water_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Discharge_Temperature_Low_Reset_Setpoint
	
	
