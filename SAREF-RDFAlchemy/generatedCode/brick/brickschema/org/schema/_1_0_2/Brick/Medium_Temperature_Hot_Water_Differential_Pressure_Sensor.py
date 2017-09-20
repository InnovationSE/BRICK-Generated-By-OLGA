from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Differential_Temperature_Sensor import Differential_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Differential_Pressure_Sensor import Hot_Water_Differential_Pressure_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water import Medium_Temperature_Hot_Water


class Medium_Temperature_Hot_Water_Differential_Pressure_Sensor(Differential_Temperature_Sensor,Hot_Water_Differential_Pressure_Sensor,Medium_Temperature_Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Medium_Temperature_Hot_Water_Differential_Pressure_Sensor
	
	
