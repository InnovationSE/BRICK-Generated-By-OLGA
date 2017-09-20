from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Temperature_Setpoint import AHU_Supply_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature_Setpoint_Increase_Decrease_Step import Discharge_Air_Temperature_Setpoint_Increase_Decrease_Step
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Temperature_Setpoint import AHU_Discharge_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature_Setpoint_Increase_Decrease_Step import Supply_Air_Temperature_Setpoint_Increase_Decrease_Step


class AHU_Supply_Air_Temperature_Setpoint_Increase_Decrease_Step(AHU_Supply_Air_Temperature_Setpoint,Discharge_Air_Temperature_Setpoint_Increase_Decrease_Step,AHU_Discharge_Air_Temperature_Setpoint,Supply_Air_Temperature_Setpoint_Increase_Decrease_Step):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Supply_Air_Temperature_Setpoint_Increase_Decrease_Step
	
	
