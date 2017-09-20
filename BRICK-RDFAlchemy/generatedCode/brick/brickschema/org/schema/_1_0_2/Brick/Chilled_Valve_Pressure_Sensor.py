from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Valve_Pressure_Sensor import Valve_Pressure_Sensor


class Chilled_Valve_Pressure_Sensor(Valve_Pressure_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Valve_Pressure_Sensor
	
	
