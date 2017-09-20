from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Torque_Sensor import Torque_Sensor


class Motor_Torque_Sensor(Torque_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Motor_Torque_Sensor
	
	
