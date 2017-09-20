from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Temperature_Cooling_Setpoint import AHU_Discharge_Air_Temperature_Cooling_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint import Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Temperature_Cooling_Setpoint import AHU_Supply_Air_Temperature_Cooling_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Supply_Air_Temperature_Dead_Band_Setpoint import Cooling_Supply_Air_Temperature_Dead_Band_Setpoint


class AHU_Cooling_Supply_Air_Temperature_Dead_Band_Setpoint(AHU_Discharge_Air_Temperature_Cooling_Setpoint,Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint,AHU_Supply_Air_Temperature_Cooling_Setpoint,Cooling_Supply_Air_Temperature_Dead_Band_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Cooling_Supply_Air_Temperature_Dead_Band_Setpoint
	
	
