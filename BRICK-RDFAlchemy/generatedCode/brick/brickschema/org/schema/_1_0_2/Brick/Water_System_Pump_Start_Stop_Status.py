from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Water_System_Pump_Status import Water_System_Pump_Status
from brick.brickschema.org.schema._1_0_2.Brick.Pump_Start_Stop_Status import Pump_Start_Stop_Status


class Water_System_Pump_Start_Stop_Status(Water_System_Pump_Status,Pump_Start_Stop_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Water_System_Pump_Start_Stop_Status
	
	
