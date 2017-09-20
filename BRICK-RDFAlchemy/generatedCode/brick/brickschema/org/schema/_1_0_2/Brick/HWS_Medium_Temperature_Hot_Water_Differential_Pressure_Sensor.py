from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.HWS_Hot_Water_Differential_Pressure_Sensor import HWS_Hot_Water_Differential_Pressure_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Medium_Temperature_Hot_Water_Differential_Pressure_Sensor import Medium_Temperature_Hot_Water_Differential_Pressure_Sensor


class HWS_Medium_Temperature_Hot_Water_Differential_Pressure_Sensor(HWS_Hot_Water_Differential_Pressure_Sensor,Medium_Temperature_Hot_Water_Differential_Pressure_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HWS_Medium_Temperature_Hot_Water_Differential_Pressure_Sensor
	
	
