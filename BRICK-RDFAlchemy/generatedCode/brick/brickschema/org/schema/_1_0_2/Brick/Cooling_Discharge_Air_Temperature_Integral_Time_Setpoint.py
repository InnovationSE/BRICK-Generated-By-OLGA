from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Integral_Time_Setpoint import Integral_Time_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Temperature_Cooling_Setpoint import Discharge_Air_Temperature_Cooling_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Temperature_Cooling_Setpoint import Supply_Air_Temperature_Cooling_Setpoint


class Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint(Integral_Time_Setpoint,Discharge_Air_Temperature_Cooling_Setpoint,Supply_Air_Temperature_Cooling_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint
	
	
