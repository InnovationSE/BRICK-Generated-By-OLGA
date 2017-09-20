from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.VFD_Current_Sensor import VFD_Current_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Motor_Current_Sensor import Motor_Current_Sensor


class VFD_Motor_Current_Sensor(VFD_Current_Sensor,Motor_Current_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Motor_Current_Sensor
	
	
