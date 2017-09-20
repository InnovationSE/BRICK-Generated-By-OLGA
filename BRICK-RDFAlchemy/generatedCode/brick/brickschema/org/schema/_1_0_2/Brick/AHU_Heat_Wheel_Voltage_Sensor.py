from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heat_Wheel_Voltage_Sensor import Heat_Wheel_Voltage_Sensor


class AHU_Heat_Wheel_Voltage_Sensor(Heat_Wheel_Voltage_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Heat_Wheel_Voltage_Sensor
	
	
