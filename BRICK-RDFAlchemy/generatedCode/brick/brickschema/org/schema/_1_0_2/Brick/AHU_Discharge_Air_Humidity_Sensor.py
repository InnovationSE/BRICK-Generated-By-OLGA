from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Humidity_Sensor import Discharge_Air_Humidity_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Humidity_Sensor import Supply_Air_Humidity_Sensor


class AHU_Discharge_Air_Humidity_Sensor(Discharge_Air_Humidity_Sensor,Supply_Air_Humidity_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Discharge_Air_Humidity_Sensor
	
	
