from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Differential_Speed_Sensor import Differential_Speed_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Heat_Wheel_Speed_Sensor import Heat_Wheel_Speed_Sensor


class AHU_Heat_Wheel_Speed_Sensor(Differential_Speed_Sensor,Heat_Wheel_Speed_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Heat_Wheel_Speed_Sensor
	
	
