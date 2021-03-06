from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heat_Exchanger_Discharge_Water_Temperature_Integral_Time_Setpoint import Heat_Exchanger_Discharge_Water_Temperature_Integral_Time_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.HWS_Heat_Exchanger_Discharge_Water_Temperature_Setpoint import HWS_Heat_Exchanger_Discharge_Water_Temperature_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Water_Temperature_Integral_Time_Setpoint import Supply_Water_Temperature_Integral_Time_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.Heat_Exchanger_Supply_Water_Temperature_Integral_Time_Setpoint import Heat_Exchanger_Supply_Water_Temperature_Integral_Time_Setpoint
from brick.brickschema.org.schema._1_0_2.Brick.HWS_Heat_Exchanger_Supply_Water_Temperature_Setpoint import HWS_Heat_Exchanger_Supply_Water_Temperature_Setpoint


class HWS_Heat_Exchanger_Discharge_Water_Temperature_Integral_Time_Setpoint(Heat_Exchanger_Discharge_Water_Temperature_Integral_Time_Setpoint,HWS_Heat_Exchanger_Discharge_Water_Temperature_Setpoint,Supply_Water_Temperature_Integral_Time_Setpoint,Heat_Exchanger_Supply_Water_Temperature_Integral_Time_Setpoint,HWS_Heat_Exchanger_Supply_Water_Temperature_Setpoint):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HWS_Heat_Exchanger_Discharge_Water_Temperature_Integral_Time_Setpoint
	
	
