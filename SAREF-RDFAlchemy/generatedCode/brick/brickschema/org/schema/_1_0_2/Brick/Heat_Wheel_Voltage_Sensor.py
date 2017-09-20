from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Voltage_Sensor import Voltage_Sensor


class Heat_Wheel_Voltage_Sensor(Voltage_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heat_Wheel_Voltage_Sensor
	
	
