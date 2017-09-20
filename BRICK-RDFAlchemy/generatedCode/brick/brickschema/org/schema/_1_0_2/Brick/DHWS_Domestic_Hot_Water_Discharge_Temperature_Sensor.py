from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Domestic_Hot_Water_Supply_Temperature_Sensor import Domestic_Hot_Water_Supply_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Domestic_Hot_Water_Discharge_Temperature_Sensor import Domestic_Hot_Water_Discharge_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Supply_Temperature_Sensor import Hot_Water_Supply_Temperature_Sensor


class DHWS_Domestic_Hot_Water_Discharge_Temperature_Sensor(Domestic_Hot_Water_Supply_Temperature_Sensor,Domestic_Hot_Water_Discharge_Temperature_Sensor,Hot_Water_Supply_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').DHWS_Domestic_Hot_Water_Discharge_Temperature_Sensor
	
	
