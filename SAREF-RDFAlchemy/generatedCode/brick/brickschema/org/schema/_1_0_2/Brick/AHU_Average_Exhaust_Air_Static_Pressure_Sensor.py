from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Average_Exhaust_Air_Static_Pressure_Sensor import Average_Exhaust_Air_Static_Pressure_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Exhaust_Air_Static_Pressure_Sensor import AHU_Exhaust_Air_Static_Pressure_Sensor


class AHU_Average_Exhaust_Air_Static_Pressure_Sensor(Average_Exhaust_Air_Static_Pressure_Sensor,AHU_Exhaust_Air_Static_Pressure_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Average_Exhaust_Air_Static_Pressure_Sensor
	
	
