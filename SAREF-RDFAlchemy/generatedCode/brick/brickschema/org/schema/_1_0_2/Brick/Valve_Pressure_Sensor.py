from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pressure_Sensor import Pressure_Sensor


class Valve_Pressure_Sensor(Pressure_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Valve_Pressure_Sensor
	
	
