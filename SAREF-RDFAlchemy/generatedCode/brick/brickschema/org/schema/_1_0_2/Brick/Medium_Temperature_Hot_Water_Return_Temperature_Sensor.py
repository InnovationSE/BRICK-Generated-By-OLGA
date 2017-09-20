from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water import Medium_Temperature_Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Return_Temperature_Sensor import Hot_Water_Return_Temperature_Sensor


class Medium_Temperature_Hot_Water_Return_Temperature_Sensor(Medium_Temperature_Hot_Water,Hot_Water_Return_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Return_Temperature_Sensor
	
	
