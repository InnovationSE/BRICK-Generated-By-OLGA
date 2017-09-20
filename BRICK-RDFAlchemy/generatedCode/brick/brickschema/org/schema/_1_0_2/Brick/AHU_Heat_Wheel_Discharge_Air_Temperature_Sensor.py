from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heat_Wheel_Supply_Air_Temperature_Sensor import Heat_Wheel_Supply_Air_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Temperature_Sensor import AHU_Supply_Air_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Heat_Wheel_Discharge_Air_Temperature_Sensor import Heat_Wheel_Discharge_Air_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Temperature_Sensor import AHU_Discharge_Air_Temperature_Sensor


class AHU_Heat_Wheel_Discharge_Air_Temperature_Sensor(Heat_Wheel_Supply_Air_Temperature_Sensor,AHU_Supply_Air_Temperature_Sensor,Heat_Wheel_Discharge_Air_Temperature_Sensor,AHU_Discharge_Air_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Heat_Wheel_Discharge_Air_Temperature_Sensor
	
	
