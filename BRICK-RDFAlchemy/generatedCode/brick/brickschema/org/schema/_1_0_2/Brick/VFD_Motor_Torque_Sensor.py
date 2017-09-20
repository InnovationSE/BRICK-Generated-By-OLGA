from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Motor_Torque_Sensor import Motor_Torque_Sensor


class VFD_Motor_Torque_Sensor(Motor_Torque_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Motor_Torque_Sensor
	
	
