from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Battery_Voltage_Sensor import Battery_Voltage_Sensor


class Solar_Panel_Battery_Voltage_Sensor(Battery_Voltage_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Solar_Panel_Battery_Voltage_Sensor
	
	
