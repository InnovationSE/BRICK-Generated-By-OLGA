from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Air_Temperature import Air_Temperature
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_System_Enable import Hot_Water_System_Enable


class Enable_Hot_Water_System_Air_Temperature(Air_Temperature,Hot_Water_System_Enable):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Enable_Hot_Water_System_Air_Temperature
	
	
