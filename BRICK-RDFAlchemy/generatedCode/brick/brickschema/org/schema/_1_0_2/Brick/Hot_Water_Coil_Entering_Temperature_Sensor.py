from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water import Hot_Water
from brick.brickschema.org.schema._1_0_2.Brick.Entering_Water_Temperature_Sensor import Entering_Water_Temperature_Sensor


class Hot_Water_Coil_Entering_Temperature_Sensor(Hot_Water,Entering_Water_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Hot_Water_Coil_Entering_Temperature_Sensor
	
	