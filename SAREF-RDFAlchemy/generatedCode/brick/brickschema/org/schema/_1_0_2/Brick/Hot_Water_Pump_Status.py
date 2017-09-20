from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pump_Status import Pump_Status
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Pump import Hot_Water_Pump


class Hot_Water_Pump_Status(Pump_Status,Hot_Water,Hot_Water_Pump):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Pump_Status
	
	
