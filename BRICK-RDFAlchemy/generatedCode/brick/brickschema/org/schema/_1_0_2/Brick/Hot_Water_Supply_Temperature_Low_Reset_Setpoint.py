from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Low_Reset_Setpoint import Temperature_Low_Reset_Setpoint


class Hot_Water_Supply_Temperature_Low_Reset_Setpoint(Temperature_Low_Reset_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Supply_Temperature_Low_Reset_Setpoint
	
	
