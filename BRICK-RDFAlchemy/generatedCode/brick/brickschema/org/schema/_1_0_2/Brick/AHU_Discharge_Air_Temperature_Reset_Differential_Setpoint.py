from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Temperature_Setpoint import AHU_Discharge_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature_Reset_Differential_Setpoint import Supply_Air_Temperature_Reset_Differential_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Temperature_Setpoint import AHU_Supply_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature_Reset_Differential_Setpoint import Discharge_Air_Temperature_Reset_Differential_Setpoint


class AHU_Discharge_Air_Temperature_Reset_Differential_Setpoint(AHU_Discharge_Air_Temperature_Setpoint,Supply_Air_Temperature_Reset_Differential_Setpoint,AHU_Supply_Air_Temperature_Setpoint,Discharge_Air_Temperature_Reset_Differential_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Discharge_Air_Temperature_Reset_Differential_Setpoint
	
	