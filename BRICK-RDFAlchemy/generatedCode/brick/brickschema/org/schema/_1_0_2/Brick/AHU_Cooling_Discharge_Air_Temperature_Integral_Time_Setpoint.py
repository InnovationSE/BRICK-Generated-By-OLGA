from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint import Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Temperature_Cooling_Setpoint import AHU_Supply_Air_Temperature_Cooling_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Temperature_Cooling_Setpoint import AHU_Discharge_Air_Temperature_Cooling_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Supply_Air_Temperature_Integral_Time_Setpoint import Cooling_Supply_Air_Temperature_Integral_Time_Setpoint


class AHU_Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint(Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint,AHU_Supply_Air_Temperature_Cooling_Setpoint,AHU_Discharge_Air_Temperature_Cooling_Setpoint,Cooling_Supply_Air_Temperature_Integral_Time_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint
	
	
