from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.AHU_Discharge_Air_Temperature_Setpoint import AHU_Discharge_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Supply_Air_Temperature_Proportional_Band_Setpoint import Economizer_Supply_Air_Temperature_Proportional_Band_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.AHU_Supply_Air_Temperature_Setpoint import AHU_Supply_Air_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Discharge_Air_Temperature_Proportional_Band_Setpoint import Economizer_Discharge_Air_Temperature_Proportional_Band_Setpoint


class AHU_Economizer_Supply_Air_Temperature_Proportional_Band_Setpoint(AHU_Discharge_Air_Temperature_Setpoint,Economizer_Supply_Air_Temperature_Proportional_Band_Setpoint,AHU_Supply_Air_Temperature_Setpoint,Economizer_Discharge_Air_Temperature_Proportional_Band_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Economizer_Supply_Air_Temperature_Proportional_Band_Setpoint
	
	
