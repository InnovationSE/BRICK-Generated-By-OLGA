from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Temperature_Setpoint import AHU_Supply_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Temperature_Setpoint import AHU_Discharge_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Min_Supply_Air_Temperature_Setpoint import Min_Supply_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Min_Discharge_Air_Temperature_Setpoint import Min_Discharge_Air_Temperature_Setpoint


class AHU_Min_Supply_Air_Temperature_Setpoint(AHU_Supply_Air_Temperature_Setpoint,AHU_Discharge_Air_Temperature_Setpoint,Min_Supply_Air_Temperature_Setpoint,Min_Discharge_Air_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Min_Supply_Air_Temperature_Setpoint
	
	
