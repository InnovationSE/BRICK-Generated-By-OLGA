from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Water_Discharge_Temperature_Sensor import Water_Discharge_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Water_Supply_Temperature_Sensor import Water_Supply_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Water_Temperature_Sensor import Supply_Water_Temperature_Sensor


class Heat_Exchanger_Supply_Water_Temperature_Sensor(Water_Discharge_Temperature_Sensor,Water_Supply_Temperature_Sensor,Supply_Water_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heat_Exchanger_Supply_Water_Temperature_Sensor
	
	
