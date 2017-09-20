from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pump_Start_Stop import Pump_Start_Stop
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Pump import Hot_Water_Pump


class Hot_Water_Pump_Start_Stop(Pump_Start_Stop,Hot_Water_Pump):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Pump_Start_Stop
	
	
