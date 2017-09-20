from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.DC_Bus_Voltage_Sensor import DC_Bus_Voltage_Sensor


class VFD_DC_Bus_Voltage_Sensor(DC_Bus_Voltage_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_DC_Bus_Voltage_Sensor
	
	
