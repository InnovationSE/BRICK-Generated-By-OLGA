from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Air_Static_Pressure_Sensor import Exhaust_Air_Static_Pressure_Sensor


class Average_Exhaust_Air_Static_Pressure_Sensor(Exhaust_Air_Static_Pressure_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Average_Exhaust_Air_Static_Pressure_Sensor
	
	