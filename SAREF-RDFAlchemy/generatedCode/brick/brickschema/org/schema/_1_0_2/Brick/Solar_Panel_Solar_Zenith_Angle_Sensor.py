from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Solar_Zenith_Angle_Sensor import Solar_Zenith_Angle_Sensor


class Solar_Panel_Solar_Zenith_Angle_Sensor(Solar_Zenith_Angle_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Solar_Panel_Solar_Zenith_Angle_Sensor
	
	
