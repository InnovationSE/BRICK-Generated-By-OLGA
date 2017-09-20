from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Pump_Lead_Lag_Command import Pump_Lead_Lag_Command


class Hot_Water_Pump_Lead_Lag_Command(Hot_Water,Pump_Lead_Lag_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Pump_Lead_Lag_Command
	
	
