from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Thermostat_Adjust_Sensor import Thermostat_Adjust_Sensor


class VAV_Thermostat_Adjust_Sensor(Thermostat_Adjust_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Thermostat_Adjust_Sensor
	
	
