from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Condensor_Temperature_Sensor import Condensor_Temperature_Sensor


class Condenser_Condensor_Temperature_Sensor(Condensor_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Condenser_Condensor_Temperature_Sensor
	
	
